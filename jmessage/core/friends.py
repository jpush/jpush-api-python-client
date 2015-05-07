#!/usr/bin/env python
# coding: utf8
from __future__ import absolute_import

from types import ListType

from jmessage.core import conf
from jmessage.core.base import BaseSDK
from jmessage.core.exceptions import ParamsError


class Friends(BaseSDK):
    """好友管理

    :param appKey: string, 应用的AppKey
    :param masterSecret: string, 相应的masterSecret
    """
    def __init__(self, appKey, masterSecret):
        super(Users, self).__init__(appKey, masterSecret)

    def get_friends_list(self, username):
        """获取某个用户好友列表

        :param username: string, 用户名
        """
        pass

    def get_friend_info(self, username, friend_username):
        """获取某个用户单个好友信息

        :param username: string, 用户名
        :param friend_username: string, 好友用户名
        """
        pass

    def batch_get_friends_info(self, username):
        """批量获取某用户好友信息

        :param username: string, 用户名
        """
        pass

    def add_friend(self, username, friend_username):
        """添加好友

        :param username: string, 用户名
        :param friend_username: string, 好友用户名
        """
        pass

    def del_friend(self, username, friend_username):
        """删除好友

        :param username: string, 用户名
        :param friend_username: string, 好友用户名
        """
        pass

    def update_friend_notename(self, username, friend_username):
        """更新好友备注

        :param username: string, 用户名
        :param friend_username: string, 好友用户名
        """
        pass
