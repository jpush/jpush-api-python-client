# -*- coding: utf-8 -*-

import json
import hashlib
import urllib
import urllib2

API_URL = "http://api.jpush.cn:8800/v2/push"
KEY_PARAMS = [
    "sendno",
    "app_key",
    "receiver_type",
    "receiver_value",
    "verification_code",
    "msg_type",
    "msg_content",
    "send_description",
    "platform",
]


class JPushClient:
    """JPush Python Client Class"""
    def __init__(self, master_secret, callback_url=""):
        self.master_secret = master_secret
        self.callback_url = callback_url

    def _gen_params(self, kargs):
        """Generate Post params"""
        params = {}
        params["callback_url"] = self.callback_url
        for k in KEY_PARAMS:
            params[k] = kargs.get(k)
        return params

    def _gen_content(self, msg_title, msg_content, msg_type, extras):
        """Generate message content"""
        content = {}
        if msg_type == 1:   # notification
            content["n_title"] = msg_title
            content["n_content"] = msg_content
            content["n_extras"] = extras
        else:           # custom message
            content["title"] = msg_title
            content["message"] = msg_content
            content["extras"] = extras
        return json.dumps(content, separators=(',', ':'))

    def _gen_verification_code(self, sendno, receiver_type, receiver_value):
        """Generage verification code"""
        mobj = hashlib.md5()
        verification_str = "%d%s%s%s" % (sendno, receiver_type,
                                         receiver_value, self.master_secret)
        mobj.update(verification_str)
        return mobj.hexdigest().upper()

    def _send_msg(self, params):
        '''Push API for all kinds of message and notification,
           dict params restore all parameters'''
        try:
            api_post = urllib2.urlopen(data=urllib.urlencode(params),
                                       url=API_URL, timeout=5)
            print api_post.read()
        except Exception, e:
            print e, e.read()

    #Deprecated"
    def send_notification_by_imei(self, imei, app_key, sendno, senddes,
                                  msg_title, msg_content, platform, extras={}):
        """Send notification by imei"""
        pass

    #Deprecated"
    def send_custom_msg_by_imei(self, imei, app_key, sendno, senddes,
                                msg_title, msg_content, platform, extras={}):
        """Send notification by imei"""
        pass

    def send_notification_by_tag(self, tag, app_key, sendno, senddes, msgtitle,
                                 msg_content, platform, extras={}):
        '''Send notification by tag'''
        receiver_type = 2
        msg_type = 1
        msg_content = self._gen_content(msgtitle, msg_content,
                                        msg_type, extras)
        receiver_value = tag
        verification_code = self._gen_verification_code(sendno,
                                                        receiver_type,
                                                        receiver_value)
        params = self._gen_params(locals())
        self._send_msg(params)

    def send_custom_msg_by_tag(self, tag, app_key, sendno, senddes,
                               msgtitle, msg_content,
                               platform, extras={}):
        '''Send custom message by tag'''
        receiver_type = 2
        msg_type = 2
        msg_content = self._gen_content(msgtitle, msg_content,
                                        msg_type, extras)
        receiver_value = tag
        verification_code = self._gen_verification_code(sendno,
                                                        receiver_type,
                                                        receiver_value)
        params = self._gen_params(locals())
        self._send_msg(params)

    def send_notification_by_alias(self, alias, app_key, sendno, senddes,
                                   msgtitle, msg_content, platform, extras={}):
        '''Send notification by alias'''
        receiver_type = 3
        msg_type = 1
        msg_content = self._gen_content(msgtitle, msg_content,
                                        msg_type, extras)
        receiver_value = alias
        verification_code = self._gen_verification_code(sendno,
                                                        receiver_type,
                                                        receiver_value)
        params = self._gen_params(locals())
        self._send_msg(params)

    def send_custom_msg_by_alias(self, alias, app_key, sendno, senddes,
                                 msgtitle, msg_content, platform, extras={}):
        '''Send custom message by alias'''
        receiver_type = 3
        msg_type = 2
        msg_content = self._gen_content(msgtitle, msg_content,
                                        msg_type, extras)
        receiver_value = alias
        verification_code = self._gen_verification_code(sendno, receiver_type,
                                                        receiver_value)
        params = self._gen_params(locals())
        self._send_msg(params)

    def send_notification_by_appkey(self, app_key, sendno, senddes, msgtitle,
                                    msg_content, platform, extras={}):
        '''Send notification by appkey'''
        receiver_type = 4
        msg_type = 1
        msg_content = self._gen_content(msgtitle, msg_content,
                                        msg_type, extras)
        receiver_value = ""
        verification_code = self._gen_verification_code(sendno, receiver_type,
                                                        receiver_value)
        params = self._gen_params(locals())
        self._send_msg(params)

    def send_custom_msg_by_appkey(self, app_key, sendno, senddes, msgtitle,
                                  msg_content, platform, extras={}):
        '''Send custom message by appkey'''
        receiver_type = 4
        msg_type = 2
        msg_content = self._gen_content(msgtitle, msg_content,
                                        msg_type, extras)
        receiver_value = ""
        verification_code = self._gen_verification_code(sendno, receiver_type,
                                                        receiver_value)
        params = self._gen_params(locals())
        self._send_msg(params)
