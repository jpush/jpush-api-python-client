import unittest
import jpush as jpush
from tests.conf import app_key, master_secret
from jpush import common

_jpush = jpush.JPush(app_key, master_secret)
schedule = _jpush.create_schedule()
_jpush.set_logging("DEBUG")

report=_jpush.create_report();


class TestEntity(unittest.TestCase):
    def test_messages(self):
        result = report.get_messages("3289406737")
        self.assertEqual(result.status_code, 200)

    def test_get_schedule_by_id(self):
        result = report.get_received("3289406737")
        self.assertEqual(result.status_code, 200)

    def test_get_schedule_by_invalid_id(self):
        try:
            result = report.get_users("DAY","2016-04-10","3")
            self.assertEqual(result.status_code, 200)
        except common.JPushFailure as e:
            self.assertIsInstance(e, common.JPushFailure)

