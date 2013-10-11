from .client import JPushClient

__version__ = '0.1.0'
VERSION = tuple(map(int,  __version__.split('.')))

__all__ = ['JPushClient']
