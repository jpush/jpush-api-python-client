#!/usr/bin/env python
# coding: utf8
"""
基于PycURL封装的简单HTTPClient

PycURL基于libcurl，而libcurl由C编写，可以提供更好的性能
基本用法:
    http = HTTPClient()
    resp = http.get('http://baidu.com')
    resp = http.post('http://baidu.com/login/',
                     params={'username': 'admin', 'password': 'admin'})
"""
import zlib
import urllib
import base64
import StringIO
from types import StringType, DictType
try:
    import json
except ImportError:
    import simplejson as json

import pycurl

from jmessage.httplib.exceptions import HeaderError, ParamsError
from jmessage.httplib.exceptions import ParseRespError, CurlError
from jmessage.httplib.utils import ParamsReader


class HTTPRequest(object):
    """HTTP Request object

    :param method: string, HTTP访问方法
    :param url: string, URL地址
    :param headers: dict, HTTP头信息, 可选
    :param params: dict, 请求参数, 可选
    :param timeout: int, 超时时间，默认10s
    """

    HTTP_GET = 'GET'
    HTTP_POST = 'POST'
    HTTP_PUT = 'PUT'
    HTTP_DELETE = 'DELETE'

    def __init__(self, method, url, **kwargs):
        self._method = method
        self._url = url
        self._headers = None
        self._params = None
        self._timeout = 10
        self._kwargs = kwargs

    def build_request(self):
        """初始化Request
        """
        self._headers = self._kwargs.pop('headers', None)
        if not isinstance(self._headers, DictType):
            raise HeaderError("HeadError, headers: %s" % self._headers)

        self._params = self._kwargs.pop('params', {})
        self._timeout = self._kwargs.pop('timeout', 300)

    def send(self):
        """发送HTTP请求
        """
        try:
            opener = pycurl.Curl()
            opener.setopt(pycurl.VERBOSE, 0)
            opener.setopt(pycurl.FOLLOWLOCATION, 1)
            opener.setopt(pycurl.MAXREDIRS, 5)
            opener.setopt(pycurl.CONNECTTIMEOUT, 60)
            opener.setopt(pycurl.TIMEOUT, self._timeout)
            opener.setopt(pycurl.SSL_VERIFYHOST, False)
            opener.setopt(pycurl.SSL_VERIFYPEER, False)

            opener.fp = StringIO.StringIO()
            opener.hd = StringIO.StringIO()
            opener.setopt(pycurl.URL, self._url)

            opener.setopt(pycurl.HTTPHEADER, ["%s: %s" % (k, v)
                          for k, v in self._headers.items()])

            opener.setopt(pycurl.ENCODING, "gzip,deflate")
            opener.setopt(pycurl.WRITEFUNCTION, opener.fp.write)
            opener.setopt(pycurl.HEADERFUNCTION, opener.hd.write)

            if self._method == 'GET':
                opener.setopt(pycurl.HTTPGET, True)
            elif self._method == 'POST':
                self._params = json.dumps(self._params)
                opener.setopt(pycurl.POST, True)
                opener.setopt(pycurl.POSTFIELDS, self._params)
            elif self._method == 'PUT':
                self._params = json.dumps(self._params)
                params_size = len(self._params)
                params_data = StringIO.StringIO(self._params)

                opener.setopt(pycurl.INFILESIZE, params_size)
                opener.setopt(pycurl.PUT, True)
                opener.setopt(pycurl.READFUNCTION,
                              ParamsReader(params_data).read)
            elif self._method == 'DELETE':
                opener.setopt(pycurl.CUSTOMREQUEST, 'DELETE')

            opener.perform()
        except pycurl.error, e:
            raise CurlError(e[0], e[1])
        else:
            self.response = self.make_reponse(opener)

        return self.response

    def make_reponse(self, opener):
        """返回HTTPResponse实例

        :param opener: pycurl.Curl实例
        """
        response = HTTPResponse(opener)
        return response


class HTTPResponse(object):
    """HTTP Response object

    :param opener: pycurl.Curl实例
    """
    def __init__(self, opener):
        self.opener = opener

        self._url = None
        self._status_code = None
        self._headers = None
        self._content = None

        self.parse_opener()

    def __repr__(self):
        return "<%s:%s>" % (self.__class__.__name__, self.status_code)

    def parse_opener(self):
        """解析opener
        """
        self._url = self.opener.getinfo(pycurl.EFFECTIVE_URL)
        self._status_code = self.opener.getinfo(pycurl.HTTP_CODE)
        self._headers = self.parse_headers()
        self._content = self.opener.fp.getvalue()

        self.opener.fp.close()
        self.opener.hd.close()
        self.opener.close()

    def parse_headers(self):
        """解析头信息d
        """
        raw_headers = self.opener.hd.getvalue()
        headers = {}
        for header in raw_headers.split('\r\n'):
            if ':' in header:
                header_list = header.split(':')
                k = header_list[0]
                v = ''.join(header_list[1:])
                headers.update({k: v})

        return headers

    @property
    def url(self):
        """返回URL地址
        """
        if not self._url:
            raise ParseRespError("URL parse error, url: %s" % self._url)

        return self._url

    @property
    def status_code(self):
        """返回响应码
        """
        if not isinstance(self._status_code, int):
            raise ParseRespError("status_code parse error,\
                    status_code: %s" % self._status_code)

        return self._status_code

    @property
    def headers(self):
        """返回头部信息
        """
        if not isinstance(self._headers, DictType):
            raise ParseRespError("headers parse error,\
                    headers: %s" % self._headers)

        return self._headers

    @property
    def content(self):
        """返回原始响应内容
        """
        if 'gzip' in self.headers.get('Content-Encoding', ''):
            try:
                self._content = self._decode_gzip(self._content)
            except Exception:
                pass

        return self._content

    @property
    def json_content(self):
        """返回JSON格式内容
        """
        try:
            return json.loads(self.content)
        except ValueError:
            return None

    def _decode_gzip(self, content):
        return zlib.decompress(content, 16 + zlib.MAX_WBITS)


class HTTPClient(object):
    """HTTP Client object

    :param appKey: string, 应用的AppKey
    :param masterSecret: string, 相应的masterSecret
    """

    def __init__(self, appKey, masterSecret):
        self.appKey = appKey
        self.masterSecret = masterSecret

    def basic_auth(self):
        """返回头部认证字符串
        """
        auth_key = "Authorization"
        auth_data = base64.encodestring("{0}:{1}".format(self.appKey,
                                                         self.masterSecret))
        auth_value = "Basic {0}".format(auth_data).strip('\n')
        return {auth_key: auth_value}

    def get(self, url, **kwargs):
        """HTTP GET 方法

        :param url: string, URL地址
        :param headers: dict, HTTP头信息, 可选
        :param params: dict, 请求参数, 可选
        :param timeout: int, 超时时间，默认10s
        """
        method = HTTPRequest.HTTP_GET
        return self.handle_request(method, url, **kwargs)

    def post(self, url, **kwargs):
        """HTTP POST 方法

        :param url: string, URL地址
        :param headers: dict, HTTP头信息, 可选
        :param params: dict, 请求参数, 可选
        :param timeout: int, 超时时间，默认10s
        """
        method = HTTPRequest.HTTP_POST
        return self.handle_request(method, url, **kwargs)

    def put(self, url, **kwargs):
        """HTTP PUT 方法

        :param url: string, URL地址
        :param headers: dict, HTTP头信息, 可选
        :param params: dict, 请求参数, 可选
        :param timeout: int, 超时时间，默认10s
        """
        method = HTTPRequest.HTTP_PUT
        return self.handle_request(method, url, **kwargs)

    def delete(self, url, **kwargs):
        """HTTP DELETE 方法

        :param url: string, URL地址
        :param headers: dict, HTTP头信息, 可选
        :param params: dict, 请求参数, 可选
        :param timeout: int, 超时时间，默认10s
        """
        method = HTTPRequest.HTTP_DELETE
        return self.handle_request(method, url, **kwargs)

    def handle_request(self, method, url, **kwargs):
        """处理HTTP请求

        :param method: string, HTTP方法
        :param url: string, URL地址
        :param headers: dict, HTTP头信息, 可选
        :param params: dict, 请求参数, 可选
        :param timeout: int, 超时时间，默认10s
        """
        # 0. 设置头信息
        kwargs = self.setup_headers(**kwargs)
        # 1. 生成请求对象 & 初始化参数
        request = HTTPRequest(method, url, **kwargs)
        request.build_request()
        # 2. 发送请求
        response = request.send()
        # 3. 返回响应对象
        return response

    def setup_headers(self, **kwargs):
        """设置头部信息

        设置Authorization、Content-Type等头部信息
        """
        auth_data = self.basic_auth()

        if 'headers' in kwargs:
            kwargs['headers'].update(auth_data)
        else:
            kwargs['headers'] = auth_data

        kwargs['headers'].update({"Content-Type": "application/json"})

        return kwargs
