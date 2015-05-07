#!/usr/bin/env python
# coding: utf8
import unittest

from base import BaseTest
import conf


class TestGroup(BaseTest):
    """测试群组相关功能
    """

    def test_get_user_groups(self):
        resp = self.sdk.groups.get_user_groups('test_group_01@py')
        self.assertEqual(resp, [conf.TEST_GROUPID])

    def test_get_group_info(self):
        resp = self.sdk.groups.get_group_info(conf.TEST_GROUPID)
        self.assertEqual(resp['gid'], conf.TEST_GROUPID)

    def test_get_group_members(self):
        resp = self.sdk.groups.get_group_members(conf.TEST_GROUPID)
        self.assertEqual(len(resp), 3)

    def test_get_app_groups(self):
        resp_default = self.sdk.groups.get_app_groups()
        assert isinstance(resp_default['groups'], list)

        resp_pagination = self.sdk.groups.get_app_groups(start=1, count=2)
        self.assertEqual(len(resp_pagination['groups']), 2)

    def test_create_group(self):
        resp = self.sdk.groups.create_group(
                'test_groups@py',
                'PyCon',
                members_username=['test_remove@py'],
                group_desc='description'
        )
        assert 'gid' in resp

    def test_update_group_members(self):
        result = self.sdk.groups.get_user_groups('test_remove@py')
        group_id = result[0]

        resp = self.sdk.groups.update_group_members(
                group_id,
                {
                    'add': ['test_add@py'],
                    'remove': ['test_remove@py']
                }
        )
        self.assertTrue(resp)

    def test_del_group(self):
        result = self.sdk.groups.get_user_groups('test_add@py')
        group_id = result[0]

        resp = self.sdk.groups.del_group(group_id)
        self.assertTrue(resp)

    def test_update_group_info(self):
        resp_exist_group = self.sdk.groups.update_group_info(
                conf.TEST_GROUPID,
                group_name='JMessage',
                group_desc='IM from JPush'
        )
        self.assertTrue(resp_exist_group)

        resp_not_exist_group = self.sdk.groups.update_group_info(
                123,
                group_name='JMessage',
                group_desc='IM from JPush'
        )
        self.assertFalse(resp_not_exist_group)
