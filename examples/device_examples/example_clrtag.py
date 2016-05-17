import jpush as jpush
from conf import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
device = _jpush.create_device()
reg_id = '090c1f59f89'
entity = jpush.device_tag("")
device.set_deviceinfo(reg_id, entity)
