from conf import app_key, master_secret
import jpush

_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")

push = _jpush.create_push()
single_payload_list = [
    {'platform':'all', 'target':'regid1', 'notification':{'alert':'alert content'}},
    {'platform':'all', 'target':'regid2', 'notification':{'alert':'alert content'}}
]
response = push.batch_push_by_regid(single_payload_list)
print(response)