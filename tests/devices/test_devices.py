import unittest
from tests.conf import app_key, master_secret
from jpush import device
from jpush import common
import jpush as jpush


_jpush = jpush.JPush(app_key, master_secret)
device = _jpush.create_device()
import logging

logging.basicConfig(level=logging.DEBUG,filename='myapp.log',filemode='w')


class TestEntity(unittest.TestCase):
    def test_create_device(self):
        reg_id = '160a3797c80d93ce897'
        entity = jpush.device_tag(jpush.add("ddd", "tageee"))
        result = device.set_devicemobile(reg_id, entity)
        self.assertEqual(result.status_code, 200)

    def test_aliasuser(self):
        alias = "alias1"
        platform = "android,ios"
        result = device.get_aliasuser(alias, platform)
        self.assertEqual(result.status_code, 200)

    def test_clear_tag(self):
        reg_id = '160a3797c80d93ce897'
        entity = jpush.device_tag("")
        try:
            device.set_deviceinfo(reg_id, entity)
        except common.JPushFailure:
            self.assertEqual(1, 1)
        except:
            self.assertEqual(1, 0)

    def test_get_device(self):
        reg_id = '160a3797c80d93ce897'
        try:
            device.get_deviceinfo(reg_id)
        except common.JPushFailure:
            self.assertEqual(1, 1)
        except:
            self.assertEqual(1, 0)

    def test_remove_alias(self):
        alias = "alias1"
        platform = "android,ios"
        result = device.delete_alias(alias, platform)
        self.assertEqual(result.status_code, 200)

    def test_remove_tags(self):
        tag = "ddd"
        platform = "android,ios"
        result = device.delete_tag(tag, platform)
        self.assertEqual(result.status_code, 200)

    def test_tag_exist(self):
        tag = "ddd"
        registration_id = '160a3797c80d93ce897'
        result = device.check_taguserexist(tag, registration_id)
        self.assertEqual(result.status_code, 200)

    def test_tag_list(self):
        result = device.get_taglist()
        self.assertEqual(result.status_code, 200)

    def test_update_tagusers(self):
        tag = "ddd"
        entity = jpush.device_regid(jpush.add("160a3797c80d93ce897"))
        result = device.update_tagusers(tag, entity)
        self.assertEqual(result.status_code, 200)

    def test_set_device_mobile(self):
        reg_id = '160a3797c80d93ce897'
        entity = jpush.device_tag(jpush.add("ddd", "tag"))
        result = device.set_devicemobile(reg_id, entity)
        self.assertEqual(result.status_code, 200)

    def test_device_mobile(self):
        reg_id = '160a3797c80d93ce897'
        entity = jpush.device_mobile("18588888888")
        result = device.set_devicemobile(reg_id, entity)
        self.assertEqual(result.status_code, 200)