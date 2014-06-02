import unittest
import sys
sys.path.append('../..')

import jpush as jpush 

class TestMessage(unittest.TestCase):

    def test_simple_alert(self):
        self.assertEqual(
            jpush.notification(alert='Hello'),
            {'alert': 'Hello'})

    def test_ios(self):
        self.assertEqual(
            jpush.notification(ios=jpush.ios(
                alert='Hello',
                badge='+1',
                sound='cat.caf',
                extra={'more': 'stuff'}
            )),
            {'ios': {
                'alert': 'Hello',
                'badge': '+1',
                'sound': 'cat.caf',
                'extra': {
                    'more': 'stuff',
                }
            }})

        self.assertEqual(
            jpush.notification(ios=jpush.ios(content_available=True)),
            {'ios': { 'content-available': True}})
