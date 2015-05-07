#!/usr/bin/env python
# coding: utf8
from __future__ import absolute_import

from types import ListType

from jmessage.core import conf
from jmessage.core.base import BaseSDK
from jmessage.core.exceptions import ParamsError


class Users(BaseSDK):
    """用户管理

    :param appKey: string, 应用的AppKey
    :param masterSecret: string, 相应的masterSecret
    """
    def __init__(self, appKey, masterSecret):
        super(Users, self).__init__(appKey, masterSecret)

    def register_users(self, user_type, user_list):
        """用户注册，包含管理员和普通用户注册

        :param user_type: string, 管理员注册时为`admin`,
                          普通用户注册时为`user`.
        :param user_list: list<dict>, 待注册用户列表
                          用户包含`username`和`password`信息
        """
        method = 'POST'

        if user_type == 'user':
            post_url = conf.REGISTER_USER
        elif user_type == 'admin':
            post_url = conf.REGISTER_ADMIN
        else:
            raise ParamsError("User type must be `user` or `admin`")

        url = self._make_url(post_url)

        if not isinstance(user_list, ListType):
            raise ParamsError("Please provide a list for\
                    register users")

        self._check_users(user_list)

        resp = self._common_process(method, url, params=user_list)
        content = self._handle_content_response(resp)
        return content

    def get_user_info(self, username):
        """根据用户名获取用户信息

        :param username: string, 用户名
        """
        self._check_username(username)

        method = 'GET'
        url = self._make_url(conf.GET_USER_INFO, username=username)
        resp = self._common_process(method, url)
        content = self._handle_content_response(resp)
        return content

    def update_user_password(self, username, new_password):
        """更新用户密码

        :param username: string, 用户名
        :param new_password: string, 新密码
        """
        self._check_username(username)      # check username
        self._check_password(new_password)  # check new_password

        method = 'PUT'
        url = self._make_url(conf.UPDATE_USER_PASSWORD, username=username)
        params = {'new_password': new_password}
        resp = self._common_process(method, url, params=params)
        status = self._handle_status_response(resp)
        return status

    def update_user_info(self, username,
                         nickname=None, birthday=None,
                         signature=None, gender=None,
                         region=None, address=None,
                         avatar=None):

        """更新用户信息

        :param username: string, 用户名
        :param nickname: string, 用户昵称, 可选
        :param birthday: string, 出生日期, 格式：1990-01-24，可选
        :param signature: string, 个性签名，可选
        :param gender: int, 性别, 男(1)，女(2)，未知(0)，可选
        :param region: string, 地区，可选
        :param address: string, 地址，可选
        :param avatar: string, 头像，可选

        以上可选参数至少设置一个
        """

        self._check_username(username)
        user_info = {
            'nickname': nickname,
            'birthday': birthday,
            'signature': signature,
            'gender': gender,
            'region': region,
            'address': address,
            'avatar': avatar
        }
        for k, v in user_info.items():
            if v is None:
                user_info.pop(k)

        # nothing to update
        if not user_info:
            raise PramsError("Nothing to update,\
                    user info parameters error.")

        method = 'PUT'
        url = self._make_url(conf.UPDATE_USER_INFO, username=username)
        resp = self._common_process(method, url, params=user_info)
        status = self._handle_status_response(resp)
        return status

    def get_users_list(self, start=0, count=100):
        """获取应用用户列表

        :param start: int, 开始位置，默认从第一个开始，即0
        :param count: int, 获取的数量，默认为100
        """
        method = 'GET'
        url = self._make_url(
            conf.GET_USER_LIST,
            start=start,
            count=count
        )
        resp = self._common_process(method, url)
        content = self._handle_content_response(resp)
        return content

    def del_user(self, username):
        """删除用户

        :param username: string, 用户名
        """
        self._check_username(username)

        method = 'DELETE'
        url = self._make_url(conf.DEL_USER, username=username)
        resp = self._common_process(method, url)
        status = self._handle_status_response(resp)
        return status
