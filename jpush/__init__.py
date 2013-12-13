from .push import JPushClient
from .recv import RecvClient

__version__ = '2.0.1'
VERSION = tuple(map(int,  __version__.split('.')))

__all__ = ['JPushClient', 'RecvClient']
