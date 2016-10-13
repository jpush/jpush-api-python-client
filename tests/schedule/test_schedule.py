import unittest
from jpush import schedule
import jpush as jpush
from jpush import common
from tests.conf import app_key, master_secret

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
        trigger = jpush.schedulepayload.trigger("2016-12-17 12:00:00")
        schedulepayload = jpush.schedulepayload.schedulepayload("name", True, trigger, push)
        result = schedule.post_schedule(schedulepayload)
        self.assertEqual(result.status_code, 200)

    def test_post_schedule_periodical(self):
        trigger = jpush.schedulepayload.trigger("12:00:00",start="2016-07-17 12:00:00", end="2016-12-17 12:00:00",
                                                time_unit = "WEEK", frequency = 1, point = ["WED","FRI"])
        schedulepayload = jpush.schedulepayload.schedulepayload("periodical", True, trigger, push)
        result = schedule.post_schedule(schedulepayload)
        self.assertEqual(result.status_code, 200)

    def test_get_schedule_by_id(self):
        result = schedule.get_schedule_by_id("a7d5ceea-8e98-11e6-8ea0-0021f652c102")
        self.assertEqual(result.status_code, 200)

    def test_get_schedule_by_invalid_id(self):
        try:
            result = schedule.get_schedule_by_id("3fc6e2fa-15a6-11e6-03d4-0021f653c222")
            self.assertNotEqual(result.status_code, 200)
        except common.JPushFailure as e:
            self.assertIsInstance(e, common.JPushFailure)

    def test_get_schedule_list(self):
        try:
            result = schedule.schedule.get_schedule_list("1")
            self.assertEqual(result.status_code, 200)
        except:
            pass

    def test_put_invalid_schedule(self):
        trigger = jpush.schedulepayload.trigger("2016-12-17 12:00:00")
        schedulepayload = jpush.schedulepayload.schedulepayload("update a new name", True, trigger, push)
        try:
            result = schedule.put_schedule(schedulepayload, "3fc6e2fa-15a6-11e6-83d4-0021f653c902")
            self.assertEqual(result.status_code, 400)
        except:
            pass

    def test_put_schedule(self):
        trigger = jpush.schedulepayload.trigger("2016-12-17 12:00:00")
        schedulepayload = jpush.schedulepayload.schedulepayload("update_a_new_name", True, trigger, push)
        try:
            result = schedule.put_schedule(schedulepayload, "3fc6e2fa-15a6-11e6-83d4-0021f653c902")
            self.assertEqual(result.status_code, 200)
        except:
            pass

    def test_delete_schedule(self):
        try:
            result = schedule.delete_schedule("59272e6a-8e98-11e6-85a9-0021f653c902")
            self.assertNotEqual(result.status_code, 200)
        except common.JPushFailure as e:
            self.assertIsInstance(e, jpush.common.JPushFailure)

