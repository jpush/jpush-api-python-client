import unittest
import jpush as jpush
from tests.conf import app_key, master_secret
from jpush import common


class TestAudience(unittest.TestCase):

    def test_basic_selectors(self):
        selectors = (
            (jpush.tag, 'tag1', {'tag': ['tag1']}),
            (jpush.tag_and, 'tag1', {'tag_and': ['tag1']}),
            (jpush.alias, 'alias1', {'alias':['alias1']}),
            (jpush.registration_id, 'regid1', {'registration_id':['regid1']}),
        )
        for selector, value, result in selectors:
            self.assertEqual(selector(value), result)

    def test_audience(self):
        _jpush = jpush.JPush(app_key, master_secret)

        push = _jpush.create_push()
        push.audience = jpush.audience(
            jpush.tag("tag1", "tag2"),
            jpush.alias("alias1", "alias2")
        )
        push.notification = jpush.notification(alert="Hello world with audience!")
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
