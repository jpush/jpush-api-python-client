import jpush as jpush
from conf import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
push = _jpush.create_push()
push.audience = jpush.audience(
            jpush.tag("tag1", "tag2"),
            jpush.alias("alias1", "alias2")
        )
push.notification = jpush.notification(alert="Hello world with audience!")
push.platform = jpush.all_
print (push.payload)
push.send()
