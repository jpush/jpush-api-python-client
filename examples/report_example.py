from conf import app_key, master_secret
import jpush

_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
report=_jpush.create_report()

def messages():
    report.get_messages("3289406737")

def messages_detail():
    report.get_messages_detail("3289406737")

def received():
    report.get_received("3289406737")

def received_detail():
    report.get_received_detail("3289406737")

def users():
    report.get_users("DAY","2016-04-10","3")

def status():
    report.get_status_message('3289406737', ['xxx'])

messages_detail()
received_detail()