import unittest
from jpush import device
import jpush as jpush
from conf import app_key, master_secret

_jpush = jpush.JPush(app_key, master_secret)
device = _jpush.create_device()


class TestEntity(unittest.TestCase):
    def test_create_device(self):
        reg_id = '1507bfd3f7c466c355c'
        entity = jpush.device_tag(jpush.add("ddd", "tageee"))
        result = device.set_devicemobile(reg_id, entity)
        self.assertEqual(result.status_code, 200)
