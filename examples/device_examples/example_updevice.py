import jpush as jpush
from conf import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
device = _jpush.create_device()
reg_id = '1507bfd3f7c466c355c'
entity = jpush.device_tag(jpush.add("ddd", "tageee"))
result=device.set_devicemobile(reg_id, entity)
print (result.status_code)
print (result.payload)