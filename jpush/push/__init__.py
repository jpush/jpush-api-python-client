from .core import Push

from .audience import (
    tag,
    tag_and,
    alias,
    registration_id,
)

from .payload import (
    android,
    ios,
    winphone,
    platform,
    notification,
    message,
    audience,
    options,
)

# Common selector for audience & platform 

all_ = "all"
"""Select all, to do a broadcast.

Used in both ``audience`` and ``platform``.
"""

__all__ = [
    all_,
    Push,
    tag,
    tag_and,
    alias,
    registration_id,
    notification,
    message,
    platform,
    audience,
    options,
]
