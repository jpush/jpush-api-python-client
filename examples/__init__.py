import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import jpush

from .conf import app_key, master_secret

from . import device_example
from . import push_example
from . import report_example
from . import schedule_example
from . import group_push_example

__all__ = [
    device_example,
    push_example,
    report_example,
    schedule_example,
    group_push_example
]
