import jpush as jpush
from conf import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
push = _jpush.create_push()
push.audience = jpush.all_
push.notification = jpush.notification(alert="Hello, world!")
push.platform = jpush.all_
push.send_validate()
