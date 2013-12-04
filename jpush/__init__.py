from .client import JPushClient

__version__ = '2.0.0'
VERSION = tuple(map(int,  __version__.split('.')))

__all__ = ['JPushClient']
