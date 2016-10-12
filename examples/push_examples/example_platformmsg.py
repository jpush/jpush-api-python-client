import jpush as jpush
from conf import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
push = _jpush.create_push()
push.audience = jpush.all_
ios_msg = jpush.ios(alert="Hello, IOS JPush!", badge="+1", sound="a.caf", extras={'k1':'v1'})
android_msg = jpush.android(alert="Hello, android msg")
push.notification = jpush.notification(alert="Hello, JPush!", android=android_msg, ios=ios_msg)
push.message=jpush.message("content",extras={'k2':'v2','k3':'v3'})
push.platform = jpush.all_
push.send()
