#!/usr/bin/env python
from jpush import common

class Device(object):
    """Device info query/update..

    """
    def __init__(self, jpush):
        self._jpush = jpush 
        self.entity = None

    def send(self, method, url, body, params, content_type=None, version=3):
        """Send the request
        
        """
        response = self._jpush._request(method, body,
            url, content_type, version=3)
        data = response.json()
        return DeviceResponse(response)

    def get_deviceinfo(self, registration_id):
        """Get deviceinfo with registration id
        """
        url = common.DEVICE_URL + registration_id
        info = self.send("GET", None, None)
        print info

class DeviceResponse(object):
    """Response to a successful device request send.

    Right now this is a fairly simple wrapper around the json payload response,
    but making it an object gives us some flexibility to add functionality
    later.

    """
    payload = None

    def __init__(self, response):
        data = response.json()
        self.payload = data

    def __str__(self):
        return "Device response Payload: {0}".format(self.payload)
