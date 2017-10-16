from . import jpush, app_key, master_secret

_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")


def huawei():
    push = _jpush.create_push()

    push.audience = jpush.all_
    push.platform = jpush.all_

    ios = jpush.ios(alert="Hello, IOS JPush!", sound="a.caf", extras={'k1':'v1'})
    android = jpush.android(alert="Hello, Android msg",
        priority=1, style=1, alert_type=1,big_text='jjjjjjjjjj',
        uri_activity='cn.jpush.android.ui.OpenClickActivity',
        extras={'k1':'v1'})

    push.notification = jpush.notification(alert="Hello, JPush!", android=android, ios=ios)

    # pprint (push.payload)
    result = push.send()

