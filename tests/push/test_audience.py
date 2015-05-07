import unittest
import jpush as jpush


class TestAudience(unittest.TestCase):

    def test_basic_selectors(self):
        selectors = (
            (jpush.tag, 'tag1', {'tag': ['tag1']}),
            (jpush.tag_and, 'tag1', {'tag_and': ['tag1']}),
            (jpush.alias, 'alias1', {'alias': ['alias1']}),
            (jpush.registration_id, 'regid1', {'registration_id': ['regid1']}),
        )
        for selector, value, result in selectors:
            self.assertEqual(selector(value), result)
