import jpush as jpush
from conf import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
schedule = _jpush.create_schedule()
schedule.get_schedule_by_id("e9c553d0-0850-11e6-b6d4-0021f652c102")
