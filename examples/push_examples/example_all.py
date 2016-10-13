import jpush as jpush
from conf import app_key, master_secret

_jpush = jpush.JPush(app_key, master_secret)

push = _jpush.create_push()

# the default logging level is WARNING,if you set the logging level to "DEBUG",the it will show the debug logging
_jpush.set_logging("DEBUG")
push.audience = jpush.all_
push.notification = jpush.notification(alert="hello python jpush api")
push.platform = jpush.all_
push.send()
