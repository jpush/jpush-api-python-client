from . import jpush
from jpush import common

group_key = u'xxxxxx'
group_secret = u'xxxxxx'

group = jpush.GroupPush(group_key, group_secret)
group.set_logging("DEBUG")

def all():
    push = group.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="!hello python jpush api")
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
