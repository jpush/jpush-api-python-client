import unittest
from jpush import schedule
import jpush as jpush
from jpush import common
from tests.conf import app_key, master_secret
import datetime

_jpush = jpush.JPush(app_key, master_secret)
schedule = _jpush.create_schedule()
# _jpush.set_logging("DEBUG")

push = _jpush.create_push()
push.audience = jpush.all_
push.notification = jpush.notification(alert="Hello, world!")
push.platform = jpush.all_
push=push.payload

now = datetime.datetime.now()
start_time = (now + datetime.timedelta(days=10)).strftime("%Y-%m-%d %H:%M:%S")
end_time = (now +datetime.timedelta(days=20)).strftime("%Y-%m-%d %H:%M:%S")

class TestEntity(unittest.TestCase):

    def test_post_schedule(self):
        trigger = jpush.schedulepayload.trigger(start_time)
        schedulepayload = jpush.schedulepayload.schedulepayload("name", True, trigger, push)
        result = schedule.post_schedule(schedulepayload)
        self.assertEqual(result.status_code, 200)

    def test_get_schedule_by_id(self):
        schedule_id = schedule.get_schedule_list("1").payload['schedules'][0]['schedule_id']
        result = schedule.get_schedule_by_id(schedule_id)
        self.assertEqual(result.status_code, 200)

    def test_get_schedule_list(self):
        result = schedule.get_schedule_list("1")
        self.assertEqual(result.status_code, 200)

    # def test_put_schedule(self):
    #     task = schedule.get_schedule_list("1").payload['schedules'][0]
    #     schedule_id = task['schedule_id']

    #     trigger = jpush.schedulepayload.trigger(task['trigger']['single']['time'])
    #     schedulepayload = jpush.schedulepayload.schedulepayload("update_a_new_name", True, trigger, push)
    #     result = schedule.put_schedule(schedulepayload, schedule_id)
    #     self.assertEqual(result.status_code, 200)
