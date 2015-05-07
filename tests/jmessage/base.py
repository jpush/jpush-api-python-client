#!/usr/bin/env python
# coding: utf8
import unittest

from jmessage import JMessageSDK
import conf


class BaseTest(unittest.TestCase):
    """测试基类
    """

    def setUp(self):
        self.sdk = JMessageSDK(conf.APPKEY, conf.MASTERSECRET)
