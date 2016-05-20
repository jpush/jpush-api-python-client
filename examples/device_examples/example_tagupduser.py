import jpush as jpush
from conf import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
device = _jpush.create_device()
tag = "ddd"
entity = jpush.device_regid(jpush.add("090c1f59f89"))
device.update_tagusers(tag, entity)
