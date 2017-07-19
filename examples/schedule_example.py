from . import jpush, app_key, master_secret

_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
schedule = _jpush.create_schedule()

def delete_schedule():
    schedule.delete_schedule("e9c553d0-0850-11e6-b6d4-0021f652c102")

def get_schedule():
    schedule.get_schedule_by_id("e9c553d0-0850-11e6-b6d4-0021f652c102")

def get_schedule():
    schedule.get_schedule_list("1")

def post_schedule():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="Hello, world!")
    push.platform = jpush.all_
    push=push.payload

    trigger=jpush.schedulepayload.trigger("2016-07-17 12:00:00")
    schedulepayload=jpush.schedulepayload.schedulepayload("name",True,trigger,push)
    result=schedule.post_schedule(schedulepayload)
    print (result.status_code)

def put_schedule():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="Hello, world!")
    push.platform = jpush.all_
    push=push.payload

    trigger=jpush.schedulepayload.trigger("2016-05-17 12:00:00")
    schedulepayload=jpush.schedulepayload.schedulepayload("update a new name", True, trigger, push)
    schedule.put_schedule(schedulepayload,"17349f00-0852-11e6-91b1-0021f653c902")
