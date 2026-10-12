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
        
    def test_hmos(self):
        self.assertEqual(
            jpush.notification(hmos=jpush.hmos(alert="Hello", title="Title", extras={'k4':'v4'})),
            {'hmos': {'extras': {'k4': 'v4'}, 'alert': 'Hello', 'title': 'Title'}}
        )

    def test_ios_interruption_level(self):
        self.assertEqual(
            jpush.ios(alert="Hello", badge="+1", sound_disable=True,
                      interruption_level="time-sensitive"),
            {'alert': 'Hello', 'badge': '+1', 'interruption-level': 'time-sensitive'}
        )

    def test_android_new_fields(self):
        self.assertEqual(
            jpush.android(
                alert="Hello",
                badge_add_num=1,
                badge_class="com.example.MainActivity",
                display_foreground="1",
                custom_buttons=[{"name": "ok", "action_type": 3}],
            ),
            {
                'alert': 'Hello',
                'badge_add_num': 1,
                'badge_class': 'com.example.MainActivity',
                'display_foreground': '1',
                'custom_buttons': [{"name": "ok", "action_type": 3}],
            }
        )

    def test_hmos_new_fields(self):
        self.assertEqual(
            jpush.hmos(
                alert="Hello",
                category="IM",
                intent={"url": "scheme://test"},
                badge_add_num=1,
                push_type=0,
                sound="service_notice.wav",
                test_message=False,
            ),
            {
                'alert': 'Hello',
                'category': 'IM',
                'intent': {"url": "scheme://test"},
                'badge_add_num': 1,
                'push_type': 0,
                'sound': 'service_notice.wav',
                'test_message': False,
            }
        )

    def test_quickapp_and_voip(self):
        self.assertEqual(
            jpush.notification(
                quickapp=jpush.quickapp(alert="Hi", title="QA", page="/page1"),
                voip={"key": "value"},
            ),
            {
                'quickapp': {'alert': 'Hi', 'title': 'QA', 'page': '/page1'},
                'voip': {'key': 'value'},
            }
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
