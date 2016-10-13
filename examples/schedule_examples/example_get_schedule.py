import jpush as jpush
from conf import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
schedule = _jpush.create_schedule()
schedule.get_schedule_by_id("8f2951c8-86cd-11e6-ae78-0021f653c902")
