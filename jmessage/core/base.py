#!/usr/bin/env python
# coding: utf8
from __future__ import absolute_import
import logging

from jmessage.core import conf
from jmessage.core.exceptions import *
from jmessage.httplib.httpclient import HTTPClient


logging.basicConfig(
    format="%(asctime)s@%(filename)s@%(lineno)s:%(message)s",
    level=logging.DEBUG
)


class BaseSDK(object):
    """处理用户、群组、消息等的基类

    :param appKey: string, 应用的AppKey
    :param masterSecret: string, 相应的masterSecret
    """
    def __init__(self, appKey, masterSecret):
        self.appKey = appKey
        self.masterSecret = masterSecret
        self.http = HTTPClient(self.appKey, self.masterSecret)

    def _check_users(self, user_list):
        """检查用户列表

        :param user_list: list<dict>, 包含多个用户的列表，
                          用户包含username、password信息.
        """
        for user in user_list:
            username = user['username']
            password = user['password']

            self._check_username(username)
            self._check_password(password)

    def _check_username(self, username):
        """检查用户名是否合适

        :param username: string, 用户名
        """
        suite_name_len = self._check_bytelen(username)
        if not suite_name_len:
            raise ParamsError("Some username's byte length is illegal,\
                    username: %s" % username)

        suite_name_limit = self._check_namerule(username)
        if not suite_name_limit:
            raise ParamsError("Username must start with num or letter,\
                    and only contain letters, numbers, `.`, `_`, `-`, `@`,\
                    user: %s" % user)

    def _check_password(self, password):
        """检查密码是否合适

        :param password: string, 密码
        """
        suite_password_len = self._check_bytelen(str(password))
        if not suite_password_len:
            raise ParamsError("Length of user's password is illegal,\
                    user: %s" % user)

    def _check_bytelen(self, str_content):
        """检查字节长度

        :param str_content: string, 待检测字符串
        """
        byte_len = len(str_content.encode('utf-8', 'ignore'))
        return byte_len >= 4 and byte_len <= 120

    def _check_namerule(self, username):
        """检查用户名是否符合命名规则

        :param username: string, 用户名
        """
        try:
            first_char = username[0]
            if not first_char.isalnum():
                return False

            for c in username:
                if c not in ('.', '_', '-', '@') and not c.isalnum():
                    return False
        except Exception, e:
            return False

        return True

    def _make_url(self, url, **kwargs):
        """生成最终的url

        :param url: string, 相关API的url模板
        :param kwargs: 可选关键字参数，根据url模板进行填充
        """
        url = "{0}{1}".format(conf.BASE_URL, url)
        return url.format(**kwargs)

    def _common_process(self, method, url, **kwargs):
        """发送HTTP请求，返回HTTP相应

        :param method: string, HTTP方法
        :param url: string, URL地址
        """
        if method == 'GET':
            response = self.http.get(url, **kwargs)
        elif method == 'POST':
            response = self.http.post(url, **kwargs)
        elif method == 'PUT':
            response = self.http.put(url, **kwargs)
        elif method == 'DELETE':
            response = self.http.delete(url, **kwargs)

        return response

    def _check_errors(self, resp, status_code):
        """检测API响应异常

        :param resp: httplib.HTTPResponse 实例
        :param status_code: int, HTTP 响应码
        """
        if status_code == 400:
            raise BadRequest(resp)
        elif status_code == 401:
            raise Unauthorized(resp)
        elif status_code == 403:
            raise Forbidden(resp)
        elif status_code == 404:
            raise NotFound(resp)
        elif status_code == 405:
            raise MethodNotAllowed(resp)
        elif 500 <= status_code < 600:
            raise SDKServerError(resp)

    def _handle_content_response(self, resp):
        """处理返回内容的请求

        :param resp: httplib.HTTPResponse 实例
        """
        status_code = resp.status_code
        try:
            self._check_errors(resp, status_code)
        except Exception, e:
            logging.debug(e)

        return resp.json_content

    def _handle_status_response(self, resp):
        """处理返回状态的请求

        :param resp: httplib.HTTPResponse 实例
        """
        status_code = resp.status_code
        try:
            self._check_errors(resp, status_code)
        except Exception, e:
            logging.debug(e)
            return False
        else:
            return True
