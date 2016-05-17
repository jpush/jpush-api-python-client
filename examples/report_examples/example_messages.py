import jpush as jpush
from conf import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
report=_jpush.create_report();
report.get_messages("3289406737")