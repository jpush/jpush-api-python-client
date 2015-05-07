#!/usr/bin/env python
# coding: utf8
from core.users import Users as UserSDK
from core.groups import Groups as GroupSDK
from core.messages import Messages as MessageSDK
from core.friends import Friends as FriendSDK

__version__ = '0.0.1'
VERSION = tuple(map(int,  __version__.split('.')))


class JMessageSDK(object):
    """JMessage各个模块操作集合

    :param appKey: string, 应用的AppKey
    :param masterSecret: string, 相应的masterSecret
    """

    def __init__(self, appKey, masterSecret):
        self.appKey = appKey
        self.masterSecret = masterSecret

    @property
    def users(self):
        return UserSDK(self.appKey, self.masterSecret)

    @property
    def groups(self):
        return GroupSDK(self.appKey, self.masterSecret)

    @property
    def messages(self):
        return MessageSDK(self.appKey, self.masterSecret)

    @property
    def friends(self):
        return FriendSDK(self.appKey, self.masterSecret)


__all__ = ['UserSDK', 'GroupSDK', 'MessageSDK', 'FriendSDK', 'JMessageSDK']
