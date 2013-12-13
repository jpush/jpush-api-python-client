# -*- coding: utf-8 -*-

import time

from jpush import JPushClient


sendno = int(time.time())
app_key = 'appkey'
master_secret = 'master_secret'

jpush_client = JPushClient(master_secret)

# Send message by tag
jpush_client.send_notification_by_tag('tagapi', app_key, sendno, 'des',
                                      'tag notify title',
                                      'tag notify content', 'android')
jpush_client.send_custom_msg_by_tag('tagapi', app_key, sendno, 'des',
                                    'tag msg title',
                                    'tag msg content', 'android')

# Send message by alias
jpush_client.send_notification_by_alias('aliasapi', app_key, sendno, 'des',
                                        'alias notify title',
                                        'alias notify content', 'android')
jpush_client.send_custom_msg_by_alias('aliasapi', app_key, sendno, 'des',
                                      'alais msg title',
                                      'alias msg content', 'android')

# Send message by app_key
jpush_client.send_notification_by_appkey(app_key, sendno, 'des',
                                         'appkey notify title',
                                         'appkey notify content', 'android')
jpush_client.send_custom_msg_by_appkey(app_key, sendno, 'des',
                                       'appkey msg title',
                                       'appkey msg content', 'android')
