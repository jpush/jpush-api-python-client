#!/usr/bin/env python
# coding: utf8
from __future__ import absolute_import
from types import ListType, DictType

from jmessage.core import conf
from jmessage.core.base import BaseSDK
from jmessage.core.exceptions import ParamsError


class Groups(BaseSDK):
    """群组管理API

    :param appKey: string, 应用的AppKey
    :param masterSecret: string, 相应的masterSecret
    """

    def __init__(self, appKey, masterSecret):
        super(Groups, self).__init__(appKey, masterSecret)

    def get_user_groups(self, username):
        """根据用户名获取群组列表

        :param username: string, 用户名
        """
        self._check_username(username)

        method = 'GET'
        url = self._make_url(conf.GET_USER_GROUPS, username=username)
        resp = self._common_process(method, url)
        content = self._handle_content_response(resp)
        return content

    def get_group_info(self, group_id):
        """根据群组ID获取群组信息

        :param group_id: int, 群组ID
        """
        method = 'GET'
        url = self._make_url(conf.GET_GROUP_INFO, gid=group_id)
        resp = self._common_process(method, url)
        content = self._handle_content_response(resp)
        return content

    def get_group_members(self, group_id):
        """根据群组ID获取群组成员

        :param group_id: int, 群组ID
        """
        method = 'GET'
        url = self._make_url(conf.GET_GROUP_MEMBER_LIST, gid=group_id)
        resp = self._common_process(method, url)
        content = self._handle_content_response(resp)
        return content

    def get_app_groups(self, start=0, count=100):
        """获取应用下的群组列表

        :param start: int, 起始位置，默认从第一个开始，即0
        :param count: int, 获取数量, 默认获取100个
        """
        method = 'GET'
        url = self._make_url(
            conf.GET_APP_GROUPS,
            start=start,
            count=count
        )
        resp = self._common_process(method, url)
        content = self._handle_content_response(resp)
        return content

    def create_group(self, owner_username, group_name,
                     members_username=[], group_desc=""):
        """创建群组

        :param owner_username: string, 群组创始人
        :param group_name: string, 群组名称
        :param members_username: list<string>, 初始成员列表, 默认为空
        :param group_desc: string, 群组简介，默认为空
        """
        method = 'POST'
        url = self._make_url(conf.CREATE_GROUP)
        params = {
            "owner_username": owner_username,
            "group_name": group_name,
            "members_username":  members_username,
            "group_desc": group_desc
        }

        resp = self._common_process(method, url, params=params)
        content = self._handle_content_response(resp)
        return content

    def update_group_members(self, group_id, op_dict):
        """添加或删除群组成员

        :param group_id: int, 群组ID
        :param op_dict: dict<list>, 成员操作信息，
                        key为`add`或`remove`, value为用户名列表
        """
        if not isinstance(op_dict, DictType):
            raise ParamsError("You should pass dict type parameters\
                    when update group members.")

        for k, v in op_dict.items():
            if k not in ('add', 'remove'):
                raise ParamsError("action must be `add` or `remove`\
                        when update group members.")
            if not isinstance(v, ListType):
                raise ParamsError("usernames must be grouped to a list\
                        when update group members.")

        method = 'POST'
        url = self._make_url(conf.UPDATE_GROUP_MEMBERS, gid=group_id)
        resp = self._common_process(method, url, params=op_dict)
        status = self._handle_status_response(resp)
        return status

    def del_group(self, group_id):
        """根据群组ID删除群组

        :param group_id: int, 群组ID
        """
        method = 'DELETE'
        url = self._make_url(conf.DEL_GROUP, gid=group_id)
        resp = self._common_process(method, url)
        status = self._handle_status_response(resp)
        return status

    def update_group_info(self, group_id, group_name=None, group_desc=None):
        """更新群组信息

        :param group_id: int, 群组ID
        :param group_name: string, 群组名称，可选
        :param group_desc: string, 群组简介，可选

        group_name和group_desc至少要设置一个
        """
        method = 'PUT'
        url = self._make_url(conf.UPDATE_GROUP_INFO, gid=group_id)

        params = {}
        if group_name is not None:
            params.update({'group_name': group_name})

        if group_desc is not None:
            params.update({'group_desc': group_desc})

        if not params:
            raise ParamsError("At least specify one of `group_name`\
                    and `group_desc`.")

        resp = self._common_process(method, url, params=params)
        status = self._handle_status_response(resp)
        return status
