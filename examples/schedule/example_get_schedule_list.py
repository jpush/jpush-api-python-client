import jpush as jpush
from conf import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)

schedule = _jpush.create_schedule()
schedule.get_schedule_list("1")