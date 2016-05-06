import unittest
from jpush import schedule
import jpush as jpush
from conf import app_key, master_secret
from jpush import common

_jpush = jpush.JPush(app_key, master_secret)
schedule = _jpush.create_schedule()
_jpush.set_logging("DEBUG")

push = _jpush.create_push()
push.audience = jpush.all_
push.notification = jpush.notification(alert="Hello, world!")
push.platform = jpush.all_
push=push.payload


class TestEntity(unittest.TestCase):
    def test_post_schedule(self):
        trigger = jpush.schedulepayload.trigger("2016-05-17 12:00:00")
        schedulepayload = jpush.schedulepayload.schedulepayload("name", True, trigger, push)
        result = schedule.post_schedule(schedulepayload)
        self.assertEqual(result.status_code, 200)

    def test_get_schedule_by_id(self):
        pass

    def test_get_schedule_list(self):
        pass

    def test_put_schedule(self):
        pass

    def test_delete_schedule(self):
        pass

