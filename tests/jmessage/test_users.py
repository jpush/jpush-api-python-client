#!/usr/bin/env python
# coding: utf8
import unittest

from base import BaseTest


class TestUser(BaseTest):
    """测试用户相关功能
    """
    def test_register_users(self):
        # 测试普通用户注册
        resp_user = self.sdk.users.register_users(
                'user',
                [
                    {'username': 'test_create@py', 'password': '123456'}
                ]
        )
        self.assertEqual(resp_user, [{'username': 'test_create@py'}])

        # 测试管理员注册
        # resp_admin = self.sdk.users.register_users('admin',
        #        [{'username': 'test_admin@py', 'password': 654321}])
        # self.assertEqual(resp_admin, [{'username': 'test_admin@py'}])

        # 测试注册已经存在的用户
        resp_exist = self.sdk.users.register_users(
                'user',
                [
                    {'username': 'test_create@py', 'password': 123456789}
                ]
        )
        assert 'error' in resp_exist[0]

    def test_get_user_info(self):
        resp = self.sdk.users.get_user_info('test_user_info@py')
        assert 'username' in resp

    def test_update_user_password(self):
        resp = self.sdk.users.update_user_password(
                'test_password@py',
                123456789
        )
        self.assertTrue(resp)

    def test_update_user_info(self):
        resp = self.sdk.users.update_user_info(
                'test_user_info@py',
                nickname='ReadTheCodes',
                birthday='1991-03-15',
                signature='I need star',
                gender=1,
                region='ShenZhen/China',
                address='ShenZhen',
                avatar='/my_avatar/'
        )
        self.assertTrue(resp)

    def test_get_users_list(self):
        resp_default = self.sdk.users.get_users_list()
        assert 'users' in resp_default

        resp_duration = self.sdk.users.get_users_list(start=1, count=1)
        assert 'users' in resp_duration

    def test_del_user(self):
        resp_create = self.sdk.users.del_user('test_create@py')
        self.assertTrue(resp_create)

        # resp_admin = self.sdk.users.del_user('test_admin@py')
        # self.assertTrue(resp_admin)
