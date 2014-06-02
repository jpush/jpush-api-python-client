import unittest
import requests
import sys
sys.path.append('../..')

import jpush as jpush


class TestPush(unittest.TestCase):

    def test_full_payload(self):
        p = jpush.Push(None)
        p.audience = jpush.all_
        p.notification = jpush.notification(alert='Hello')
        p.options = {}
        p.paltform = jpush.all_
        p.message = jpush.message("Title", "Body", "text/html", "utf8")

        self.assertEqual(p.payload, {
            "audience": "all",
            "notification": {"alert": "Hello"},
            "platform": "all",
            "options": {},
            "message": {
                "msg_content": "Hello message from jpush",
            }
        })
