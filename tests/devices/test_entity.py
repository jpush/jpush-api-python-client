import unittest
import jpush


class TestEntity(unittest.TestCase):

    def test_basic_entity(self):
        entities = (
            (jpush.add, 'tag1', {'add': ['tag1']}),
            (jpush.remove, 'tag1', {'remove': ['tag1']}),
            (jpush.device_tag, 'tag1', {'tags': 'tag1'}),
            (jpush.device_alias, 'alias1', {'alias': 'alias1'}),
            (jpush.device_regid, 'registration_id1',
                {'registration_ids': 'registration_id1'}),
        )
        for entity, value, result in entities:
            self.assertEqual(entity(value), result)

    def test_compound_entity(self):
        self.assertEqual(
            jpush.device_tag(jpush.add("tag1", "tag2")),
            {'tags': {'add': ['tag1', 'tag2']}}
        )

        self.assertEqual(
            jpush.device_tag(jpush.remove("tag1", "tag2")),
            {'tags': {'remove': ['tag1', 'tag2']}}
        )

        self.assertEqual(
            jpush.device_alias(
                jpush.add("alias1", "alias2"),
                jpush.remove("alias3", "alias4")
            ),
            {
                'alias': {
                    'add': ['alias1', 'alias2'],
                    'remove': ['alias3', 'alias4']
                }
            }
        )

        self.assertEqual(
            jpush.device_regid(
                jpush.add("regid1", "regid2"),
                jpush.remove("regid3", "regid4")
            ),
            {
                'registration_ids': {
                    'add': ['regid1', 'regid2'],
                    'remove': ['regid3', 'regid4']
                }
            }
        )
