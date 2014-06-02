import unittest
import sys
sys.path.append('../..')

import jpush as jpush 

class TestAudience(unittest.TestCase):

    def test_basic_selectors(self):
        selectors = (
            (jpush.tag, 'test', {'tag': 'test'}),
            (jpush.tag_and, 'test', {'tag_and': 'test'}),
            (jpush.alias, 'test', {'alias': 'test'}),
            (jpush.registration_id, 'test', {'registration_id': 'test'}),
        )

        for selector, value, result in selectors:
            self.assertEqual(selector(value), result)
