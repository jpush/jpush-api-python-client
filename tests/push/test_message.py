# -*- coding:utf-8 -*-
import unittest
import jpush as jpush


class TestMessage(unittest.TestCase):

    def test_simple_alert(self):
        self.assertEqual(jpush.notification(alert='中文'), {'alert': '中文'})

    def test_ios(self):
        self.assertEqual(
            jpush.notification(
                ios=jpush.ios(
                    alert="Hello",
                    badge="+1",
                    sound="a.caf",
                    extras={'k1': 'v1'}
                )
            ),
            {
                'ios': {
                    'sound': 'a.caf',
                    'extras': {'k1': 'v1'},
                    'badge': '+1',
                    'alert': 'Hello'
                }
            }
        )

    def test_iossilent(self):
        self.assertEqual(
            jpush.notification(
                ios=jpush.ios(
                    alert="Hello",
                    badge="+1",
                    extras={'k1': 'v1'},
                    sound_disable=True
                )
            ),
            {
                'ios': {
                    'extras': {'k1': 'v1'},
                    'badge': '+1',
                    'alert': 'Hello'
                }
            }
        )

    def test_android(self):
        self.assertEqual(
            jpush.notification(
                android=jpush.android(
                    alert="Hello",
                    extras={'k2': 'v2'}
                )
            ),
            {
                'android': {
                    'extras': {'k2': 'v2'},
                    'alert': 'Hello'
                }
            }
        )

    def test_winphone(self):
        self.assertEqual(
            jpush.notification(
                winphone=jpush.winphone(
                    alert="Hello",
                    extras={'k3': 'v3'}
                )
            ),
            {
                'winphone': {
                    'extras': {'k3': 'v3'},
                    'alert': 'Hello'
                }
            }
        )
