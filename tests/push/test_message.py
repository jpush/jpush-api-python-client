# -*- coding:utf-8 -*-
import unittest
import jpush as jpush
from tests.conf import app_key, master_secret
from jpush import common


class TestMessage(unittest.TestCase):

    def test_simple_alert(self):
        self.assertEqual(jpush.notification(alert='中文'), {'alert':'中文'})

    def test_ios(self):
        self.assertEqual(
            jpush.notification(ios=jpush.ios(alert="Hello", badge="+1", sound="a.caf", extras={'k1':'v1'})),
            {'ios': {'sound': 'a.caf', 'extras': {'k1': 'v1'}, 'badge': '+1', 'alert': 'Hello'}}
        )

    def test_iossilent(self):
        self.assertEqual(
            jpush.notification(ios=jpush.ios(alert="Hello", badge="+1", extras={'k1':'v1'}, sound_disable=True)),
            {'ios': {'extras': {'k1': 'v1'}, 'badge': '+1', 'alert': 'Hello'}}
        )

    def test_android(self):
        self.assertEqual(
            jpush.notification(android=jpush.android(alert="Hello", extras={'k2':'v2'})),
            {'android': {'extras': {'k2': 'v2'}, 'alert': 'Hello'}}
        )

    def test_winphone(self):
        self.assertEqual(
            jpush.notification(winphone=jpush.winphone(alert="Hello", extras={'k3':'v3'})),
            {'winphone': {'extras': {'k3': 'v3'}, 'alert': 'Hello'}}
        )

    def test_push(self):
        _jpush = jpush.JPush(app_key, master_secret)
        push = _jpush.create_push()
        push.audience = jpush.all_
        push.notification = jpush.notification(alert="hello python jpush api")
        push.platform = jpush.all_
        try:
            response = push.send()
            self.assertEqual(response.status_code, 200)
        except common.Unauthorized as e:
            self.assertFalse(isinstance(e, common.Unauthorized))
            raise common.Unauthorized("Unauthorized")
        except common.APIConnectionException as e:
            self.assertFalse(isinstance(e, common.APIConnectionException))
            raise common.APIConnectionException("conn")
        except common.JPushFailure as e:
            self.assertFalse(isinstance(e, common.JPushFailure))
            print ("JPushFailure")
        except:
            self.assertFalse(1)
            print ("Exception")
