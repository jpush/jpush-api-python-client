#!/usr/bin/env python
# coding: utf8
from jmessage import JMessageSDK
import conf

sdk = JMessage(conf.APPKEY, conf.MASTERSECRET)


def create_group():
    """创建群组

    resp example:
    {
        "gid":12345,
        "owner_username": 'example_group_owner@py',
        "group_name": "PyCon",
        "members_username": ['example_user_01@py', 'example_user_02@py'],
        "group_desc":"Conf for Pythonista!",
        "level" = 3,
        "mtime" = "2014-07-01 00:00:00",
        "ctime"="2014-06-05 00:00:00"
    }
    """

    resp = sdk.groups.create_group(
        'example_group_owner@py',    # 群组创始人
        'PyCon',                     # 群组名称
        # 初始成员列表
        members_username=['example_user_01@py', 'example_user_02@py'],
        group_desc="Conf for Pythonista!"    # 群组简介
    )

    group_id = resp['gid']           # 你成功创建的群组ID
    return group_id


def get_group_info(group_id):
    """获取群组详情

    resp: resp的格式同上
    """
    resp = sdk.groups.get_group_info(group_id)
    return resp


def update_group_info(group_id, group_name=None, group_desc=None):
    """更新群组信息

    params: group_name和group_desc二者至少要设置一个
    resp: 更新成功返回`True`, 否则返回`False`
    """

    resp = sdk.groups.update_group_info(
        group_id,
        group_name=group_name,
        group_desc=group_desc
    )

    return resp


def del_group(group_id):
    """删除群组

    resp: 删除成功返回`True`, 否则返回`False`
    """
    resp = sdk.groups.del_group(group_id)

    return resp


def get_user_groups(username):
    """获取某用户所在群组列表

    resp: resp为一个list，包含该用户所在的群组ID
    """
    resp = sdk.groups.get_user_groups(username)

    return resp


def update_group_members(group_id, add_list=None, remove_list=None):
    """管理群组成员
    add_list: 需要增加的用户名列表
    remove_list: 需要删除的用户名列表

    resp: 更新成功返回`True`, 否则返回`False`
    """
    op_dict = {}

    if add_list is not None:
        op_dict.update({'add': add_list})

    if remove_list is not None:
        op_dict.update({'remove': remove_list})

    resp = sdk.groups.update_group_members(group_id, op_dict)

    return resp


def get_group_members(group_id):
    """获取群组成员

    resp example:
    [
        {
            "username": "asdf",
            "flag": 0,
            "ctime": "2010-10-01 10:10:10"
        },
        {
            "username": "test",
            "flag": 1,
            "ctime": "2010-10-01 10:10:10"
        }
    ]

    flag: 1表示群主，0表示普通成员
    """

    resp = sdk.groups.get_group_members(group_id)

    return resp


def get_app_groups(start=0, count=100):
    """获取应用下的群组

    resp example:
    {
        "total":1233,
        "start":1100,
        "count":100,
        "groups": [10000000, 1000000001, ...]
    }
    """

    resp = sdk.groups.get_app_groups(start=start, count=count)

    return resp
