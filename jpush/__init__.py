"""Python package for using the JPush API"""
from .core import JPush
from .common import JPushFailure, Unauthorized

__version__ = '3.1.2'
VERSION = tuple(map(int,  __version__.split('.')))

from .push import (
    Push,
    all_,
    tag,
    tag_and,
    alias,
    registration_id,
    notification,
    ios,
    android,
    winphone,
    platform,
    audience,
    options,
    message,
    smsmessage,
)

from .device import (
    Device,
    add,
    remove,
    device_tag,
    device_alias,
    device_regid,
    device_mobile,
)

from .report import (
    Report,
)

__all__ = [
    JPush,
    JPushFailure,
    Unauthorized,
    all_,
    Push,
    tag,
    tag_and,
    alias,
    registration_id,
    notification,
    ios,
    android,
    winphone,
    message,
    smsmessage,
    platform,
    audience,
    options,
    Device,
    add,
    remove,
    device_tag,
    device_alias,
    device_regid,
    Report,
]

# Silence urllib3 INFO logging by default

import logging
logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.WARNING)
