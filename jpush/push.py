# -*- coding: utf-8 -*-
#
# Push API
#

import base64
import json
import hashlib
import urllib
import urllib2

API_URL = "https://api.jpush.cn/v3/push"

class JPushClient:
    """JPush Python Client Class"""
    def __init__(self, app_key, master_secret):
        self.app_key = app_key
        self.master_secret = master_secret

    def _send_msg(self, params):
        '''Push API for all kinds of message and notification,
           dict params restore all parameters'''
        try:
            send_param=json.dumps(params)
        except Exception as e:
            print 'params should be json object ', e

        try:
            base64string = base64.encodestring('%s:%s' % (self.app_key, self.master_secret))[:-1]
            req = urllib2.Request(API_URL)
            req.add_header("Authorization", "Basic %s" % base64string)
            api_post = urllib2.urlopen(req,  urllib.urlencode(params), timeout=5)
            print api_post.read()
        except Exception as e:
            print 'send message fail ', e
    
    def send_msg(self, params):
        '''Push API for message send.
           params must be json-format string;'''
        try:
            self._send_msg(params)
        except Exception as e:
            print e
