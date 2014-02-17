# -*- coding: utf-8 -*-
'''Test sending msg by registration id'''
import time
from jpush import JPushClient

sendno = int(time.time())
app_key = 'dd1066407b044738b6479275'
master_secret = '2b38ce69b1de2a7fa95706ea'

jpush_client = JPushClient(master_secret)
reg_id = '0900e8d85ef'

jpush_client.send_notification_by_registrationid(reg_id, app_key, sendno, 'des',
                                        'registration id notify title',
                                        'registration id notify content', 'android')
