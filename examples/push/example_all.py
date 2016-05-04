import jpush as jpush
from jpush import core
from conf import app_key, master_secret
from jpush import common

_jpush = jpush.JPush(app_key, master_secret)

push = _jpush.create_push()
push.audience = jpush.all_
push.notification = jpush.notification(alert="hello python jpush api")
push.platform = jpush.all_
core.logger.debug('logger debug message test')
try:
    response=push.send()
except common.Unauthorized:
    raise common.Unauthorized("Unauthorized")
except common.APIConnectionException:
    raise common.APIConnectionException("conn")


