import jpush as jpush
from conf import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)

device = _jpush.create_device()
alias = "alias1"
platform = "android,ios"
device.get_aliasuser(alias, platform)
