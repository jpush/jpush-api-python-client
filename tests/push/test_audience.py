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

    def test_invalid_device_selectors(self):
        selectors = (
            (jpush.device_token, 'f' * 63),
            (jpush.device_token, 'f' * 65),
            (jpush.device_token, '0123'),
            (jpush.device_token, 'X' * 64),
            (jpush.device_pin, '1234567'),
            (jpush.device_pin, 'x' * 8),
            (jpush.apid, 'foobar'),
            (jpush.apid, '074e84a2-9ed9-4eee-9ca4-cc597bfdbef33'),
            (jpush.apid, '074e84a2-9ed9-4eee-9ca4-cc597bfdbef'),
            (jpush.wns, '074e84a2-9ed9-4eee-9ca4-cc597bfdbef'),
            (jpush.mpns, '074e84a2-9ed9-4eee-9ca4-cc597bfdbef'),
        )

        for selector, value in selectors:
            self.assertRaises(ValueError, selector, value)

    def test_compound_selectors(self):
        self.assertEqual(
            jpush.or_(jpush.tag('foo'), jpush.tag('bar')),
            {'or': [{'tag': 'foo'}, {'tag': 'bar'}]})

        self.assertEqual(
            jpush.and_(jpush.tag('foo'), jpush.tag('bar')),
            {'and': [{'tag': 'foo'}, {'tag': 'bar'}]})

        self.assertEqual(
            jpush.not_(jpush.tag('foo')),
            {'not': {'tag': 'foo'}})
