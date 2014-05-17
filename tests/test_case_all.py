#-*- coding: utf-8 -*-

'''Test sending msg'''
import time
import sys
import json

sys.path.append("..")
from jpush import JPushClient

sendno = int(time.time())
app_key = 'dd1066407b044738b6479275'
master_secret = '2b38ce69b1de2a7fa95706ea'

msg_json = '''{"platform":"android,ios,winphone","audience":"all","notification":{"android":{"alert":"android 内容发送时间%s","title":"android 标题","builder_id":2,"extras":{"android jian1键":"android zhi1值","android jian2":"android zhi2"}},"ios":{"alert":"ios推送内容","sound":"sound.caf","badge":2,"content-avaliable":1},"winphone":{"alert":"winphone 内容","title":"WinPhone title","_open_page":"Page1.xaml","extras":{"winphone key1":"winphone value1"}}},"options":{"time_to_live":60, "sendno":%d}}''' %(time.strftime("%Y%m%d %H:%M:%S"), sendno)
msg_json = json.loads(msg_json)

print msg_json

jpush_client = JPushClient(app_key, master_secret)
jpush_client.send_msg(msg_json)
