#!/usr/bin/env python
from jpush import common
import json
import base64
from hyper import HTTP20Connection
import logging

logger = logging.getLogger('jpush')

class Device(object):
    """Device info query/update..

    """
    def __init__(self, jpush):
        self._jpush = jpush 
        self.entity = None


    def _request(self, method, body, url,base_url=None):
        headers = {}
        headers['user-agent'] = 'jpush-api-python-client'
        headers['connection'] = 'keep-alive'
        headers['content-type'] = 'application/json;charset:utf-8'

        logger.debug("Making %s request to %s. Headers:\n\t%s\nBody:\n\t%s",
                     method, url, '\n\t'.join('%s: %s' % (key, value) for (key, value) in headers.items()), body)
        base64string = base64.encodestring('%s:%s' % (self.key, self.secret))[:-1]
        authheader = "Basic %s" % base64string
        headers['Authorization'] = authheader
        conn = HTTP20Connection(host=base_url, secure=True)

        response = conn.request(method,url,headers=headers,body=body)
        resp = conn.get_response(response)
        logger.debug(resp.status)
        logger.debug(resp.read())
        return resp


    def get_taglist(self):
        """Get deviceinfo with registration id.
        """
        url = common.TAGLIST_URL
        body = None
        info = self._jpush._request('GET',body,url,base_url=common.DEVICE_BASEURL)
        return info

    def get_deviceinfo(self, registration_id):
        """Get deviceinfo with registration id.
        """
        url = common.DEVICE_URL + registration_id + "/"
        body = None
        info = self._jpush._request('GET', body, url, base_url=common.DEVICE_BASEURL)
        return info

    def set_deviceinfo(self, registration_id, entity):
        """Update deviceinfo with registration id.
        """
        url = common.DEVICE_URL + registration_id + "/"
        body = json.dumps(entity)
        info = self._jpush._request('POST', body, url, base_url=common.DEVICE_BASEURL)
        return info

    def set_devicemobile(self, registration_id, entity):
        """Update deviceinfo with registration id.
        """
        url = common.DEVICE_URL + registration_id + "/"
        body = json.dumps(entity)
        info = self._jpush._request('POST', body, url, base_url=common.DEVICE_BASEURL)
        return info

    def delete_tag(self, tag, platform=None):
        """Delete registration id tag.
        """
        url = common.TAG_URL + tag + "/"
        body = None
        if platform:
            body = platform
        info = self._jpush._request('DELETE', body, url, base_url=common.DEVICE_BASEURL)
        return info

    def update_tagusers(self, tag, entity):
        """Add/Remove specified tag users.
        """
        url = common.TAG_URL + tag + "/"
        body = json.dumps(entity)
        info = self._jpush._request('POST', body, url, base_url=common.DEVICE_BASEURL)
        return info

    def check_taguserexist(self, tag, registration_id):
        """Check registration id whether in tag.
        """
        url = common.TAG_URL + tag + "/registration_ids/" + registration_id
        body = registration_id
        info = self._jpush._request('GET', body, url, base_url=common.DEVICE_BASEURL)
        return info

    def delete_alias(self, alias, platform=None):
        """Delete appkey alias.
        """
        url = common.ALIAS_URL + alias + "/"
        body = None
        if platform:
            body = platform
        info = self._jpush._request('DELETE', body, url, base_url=common.DEVICE_BASEURL)
        return info

    def get_aliasuser(self, alias, platform=None):
        """Get appkey alias users.
        """
        url = common.ALIAS_URL + alias + "/"
        body = None
        if platform:
            body = platform
        info = self._jpush._request('GET', body, url, base_url=common.DEVICE_BASEURL)
        return info


class DeviceResponse(object):
    """Response to a successful device request send.

    Right now this is a fairly simple wrapper around the json payload response,
    but making it an object gives us some flexibility to add functionality
    later.

    """
    payload = None
    status_code = None

    def __init__(self, response):
        self.status_code = response.status_code
        if 0 != len(response.content):
            data = response.json()
            self.payload = data
        elif 200 == response.status_code:
            self.payload = "success"

    def get_status_code(self):
        return self.status_code

    def __str__(self):
        return "Device response Payload: {0}".format(self.payload)
