from . import jpush, app_key, master_secret

_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
report=_jpush.create_report()

def messages():
    report.get_messages("3289406737")

def receivede():
    report.get_received("3289406737")

def users():
    report.get_users("DAY","2016-04-10","3")
