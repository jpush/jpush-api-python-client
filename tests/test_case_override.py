# -*- coding: utf-8 -*-
'''Test sending msg'''
import time
import sys
sys.path.append("..")
from jpush import JPushClient

sendno = int(time.time())
app_key = 'dd1066407b044738b6479275'
master_secret = '2b38ce69b1de2a7fa95706ea'
msg_json = {"platform":"all","audience":"all", "notification":{"alert":"Pall Nall alert"},"options":{"time_to_live":60, "sendno":sendno, "override_msg_id":1154755988}}

print msg_json

jpush_client = JPushClient(app_key, master_secret)
jpush_client.send_msg(msg_json)
