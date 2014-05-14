# -*- coding: utf-8 -*-

import time

from jpush import JPushClient
import conf

sendno = int(time.time())
app_key = conf.APP_KEY
master_secret = conf.MASTER_SECRET

jpush_client = JPushClient(master_secret)

# Send message
jpush_client.send_msg(msg_json)
