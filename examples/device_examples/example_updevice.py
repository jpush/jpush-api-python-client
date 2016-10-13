import jpush as jpush
from conf import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
device = _jpush.create_device()
reg_id = '160a3797c80d93ce897'
entity = jpush.device_tag(jpush.add("ddd", "tageee"))
result=device.set_devicemobile(reg_id, entity)
print (result.status_code)