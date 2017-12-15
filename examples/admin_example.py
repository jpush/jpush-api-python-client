from . import jpush, dev_key, dev_secret

admin = jpush.Admin(dev_key, dev_secret)
admin.set_logging("DEBUG")

def create_app():
    response = admin.create_app('aaa', 'cn.jpush.app')
    return response

def delete_app(app_key):
    response = admin.delete_app(app_key)
    return response
