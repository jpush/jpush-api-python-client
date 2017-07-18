from . import jpush, app_key, master_secret

_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
device = _jpush.create_device()

def alias_user():
    alias = "alias1"
    platform = "android,ios"
    device.get_aliasuser(alias, platform)

def ctrl_tag():
    reg_id = '090c1f59f89'
    entity = jpush.device_tag("")
    device.set_deviceinfo(reg_id, entity)

def get_device():
    reg_id = '090c1f59f89'
    device.get_deviceinfo(reg_id)

def delete_alias():
    alias = "alias1"
    platform = "android,ios"
    device.delete_alias(alias, platform)

def delete_tag():
    tag = "ddd"
    platform = "android,ios"
    device.delete_tag(tag, platform)

def check_tag():
    tag = "ddd"
    registration_id = '090c1f59f89'
    device.check_taguserexist(tag, registration_id)

def tag_list():
    device.get_taglist()

def tag_update_user():
    tag = "ddd"
    entity = jpush.device_regid(jpush.add("090c1f59f89"))
    device.update_tagusers(tag, entity)

def update_device():
    reg_id = '1507bfd3f7c466c355c'
    entity = jpush.device_tag(jpush.add("ddd", "tageee"))
    result=device.set_devicemobile(reg_id, entity)
    print (result.status_code)
    print (result.payload)

def update_device_mobile():
    reg_id = '1507bfd3f7c466c355c'
    entity = jpush.device_mobile("18588232140")
    device.set_devicemobile(reg_id, entity)
