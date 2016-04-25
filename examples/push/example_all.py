import jpush as jpush
from jpush import core
from conf import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)

push = _jpush.create_push()
push.audience = jpush.all_
push.notification = jpush.notification(alert="Hello,python sdk!")
push.platform = jpush.all_
core.logger.debug('logger debug message test')
push.send()
