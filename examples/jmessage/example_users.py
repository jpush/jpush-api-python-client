#!/usr/bin/env python
# coding: utf8

from jmessage import JMessageSDK
import conf

sdk = JMessage(conf.APPKEY, conf.MASTERSECRET)


def register_users(user_type, users_list):
    """注册用户

    注册普通用户时user_type为`user`，注册管理员时user_type为`admin`
    users_list为包含用户信息的列表，例如:
    [
        {"username": "dev_fang", "password": "password"},
        {"username": "dev_fang", "password": "password"}
    ]

    resp为一个列表，列表里面为一个字典，包含`username`，
    注册失败的用户包含error信息，例如：
    [
        {
            "username": "dev_fang"
        },
        {
            "username": "dev_javen",
            "error": {
                "code": 8001,
                "message": "The user already exist!"
            }
        }
    ]
    """
    resp = sdk.users.register_users(user_type, users_list)

    register_success = []
    register_failed = []

    for user in resp:
        username = user['username']

        if 'error' in user:
            register_failed.append(username)
        else:
            register_success.append(username)

    # 返回注册成功和注册失败的`username`
    return register_success, register_failed


def get_user_info(username):
    """获取用户信息

    user_info example:
    {
        "username" : "javen",
        "nickname" : "hello",
        "avatar" = "/avatar",
        "birthday" : "1990-01-24 00:00:00",
        "gender" : 0,
        "signature" : "orz",
        "region" : "shenzhen",
        "address" : "shenzhen",
        "mtime" : "2015-01-01 00:00:00",
        "ctime" : "2015-01-01 00:00:00"
    }
    """

    user_info = sdk.users.get_user_info(username)
    return user_info


def update_user_password(username, new_password):
    """修改密码

    resp: 更改密码成功时返回`True`，否则返回`False`
    """

    resp = sdk.users.update_user_password('test_password@py')
    return resp


def update_user_info(username, nickname=None,
                     birthday=None, signature=None,
                     gender=None, region=None,
                     address=None, avatar=None):
    """更新用户信息

    resp: 更改用户信息成功时返回`True`，否则返回`False
    """

    resp = sdk.users.update_user_info(
        username,
        nickname=None,
        birthday=None,
        signature=None,
        gender=None,
        region=None,
        address=None,
        avatar=None
    )

    return resp


def get_users_list(start=0, count=1):
    """获取应用用户列表

    resp: 返回一个包含应用用户名的列表
    """

    resp = sdk.users.get_users_list(start=start, count=count)

    return resp


def del_user(username):
    """删除用户

    resp: 删除用户成功时返回`True`，否则返回`False
    """

    resp = sdk.users.del_user(username)

    return resp
