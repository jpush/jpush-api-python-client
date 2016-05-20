import jpush as jpush
from conf import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
device = _jpush.create_device()
tag = "ddd"
registration_id = '090c1f59f89'
device.check_taguserexist(tag, registration_id)
