import jpush as jpush
from conf import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
schedule = _jpush.create_schedule()

push = _jpush.create_push()
push.audience = jpush.all_
push.notification = jpush.notification(alert="Hello, world!")
push.platform = jpush.all_
push=push.payload

trigger=jpush.schedulepayload.trigger("2016-05-17 12:00:00")
schedulepayload=jpush.schedulepayload.schedulepayload("update a new name", True, trigger, push)
schedule.put_schedule(schedulepayload,"17349f00-0852-11e6-91b1-0021f653c902")