import jpush as jpush
from conf import app_key, master_secret
from jpush import common

_jpush = jpush.JPush(app_key, master_secret)

push = _jpush.create_push()

# the default logging level is WARNING,if you set the logging level to "DEBUG",the it will show the debug logging
_jpush.set_logging("DEBUG")
push.audience = jpush.all_
push.notification = jpush.notification(alert="hello python jpush api")
push.platform = jpush.all_
try:
    response=push.send()
except common.Unauthorized:
    raise common.Unauthorized("Unauthorized")
except common.APIConnectionException:
    raise common.APIConnectionException("conn")
except common.JPushFailure:
    print ("JPushFailure")
except:
    print ("Exception")