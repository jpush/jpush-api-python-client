# -*- coding: utf-8 -*-
'''Test sending msg'''
import time
import sys
sys.path.append("..")
from jpush import JPushClient

sendno = int(time.time())
app_key = 'dd1066407b044738b6479275'
master_secret = '2b38ce69b1de2a7fa95706ea'
msg_json = '''{"platform":"all","audience":"all", "notification":{"android":{"alert":"Pall Nandroid alert"}},"options":{"time_to_live":60, "sendno":%d}}''' %(sendno)

jpush_client = JPushClient(app_key, master_secret)
jpush_client.send_msg(msg_json)
