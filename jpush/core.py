import json
import logging
import warnings

import requests
from . import common
from .push import Push
from .device import Device
from .report import Report
from .schedule import Schedule


logger = logging.getLogger('jpush')


class JPush(object):
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.session = requests.Session()
        self.session.auth = (key, secret)

    def _request(self, method, body, url, content_type=None, version=None, params=None):
        headers = {}
        headers['user-agent'] = 'jpush-api-python-client'
        headers['connection'] = 'keep-alive'
        headers['content-type'] = 'application/json;charset:utf-8'

        logger.debug("Making %s request to %s. Headers:\n\t%s\nBody:\n\t%s",
                     method, url, '\n\t'.join('%s: %s' % (key, value) for (key, value) in headers.items()), body)
        try:
            response = self.session.request(method, url, data=body, params=params, headers=headers, timeout=30)
        except requests.exceptions.ConnectTimeout:
            raise common.APIConnectionException("Connection to api.jpush.cn timed out.")
        except:
            raise common.APIConnectionException("Connection to api.jpush.cn error.")

        logger.debug("Received %s response. Headers:\n\t%s\nBody:\n\t%s", response.status_code, '\n\t'.join(
                '%s: %s' % (key, value) for (key, value) in response.headers.items()), response.content)

        if response.status_code == 401:
            raise common.Unauthorized("Please check your AppKey and Master Secret")
        elif not (200 <= response.status_code < 300):
            raise common.JPushFailure.from_response(response)
        return response

    def push(self, payload):
        """Push this payload to the specified recipients.

        Payload: a dictionary the contents to send, e.g.:
            {'aps': {'alert': 'Hello'}, 'android': {'alert': 'Hello'}}
        """
        warnings.warn(
            "JPush.push() is deprecated. See documentation on upgrading.",
            DeprecationWarning)
        body = json.dumps(payload)
        self._request('POST', body, common.PUSH_URL, 'application/json', version=1)

    def  set_logging(self, level):
        level_list= ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"]
        if level in level_list:
            if(level == "CRITICAL"):
                logging.basicConfig(level=logging.CRITICAL)
            if (level == "ERROR"):
                logging.basicConfig(level=logging.ERROR)
            if (level == "WARNING"):
                logging.basicConfig(level=logging.WARNING)
            if (level == "INFO"):
                logging.basicConfig(level=logging.INFO)
            if (level == "DEBUG"):
                logging.basicConfig(level=logging.DEBUG)
            if (level == "NOTSET"):
                logging.basicConfig(level=logging.NOTSET)
        else:
            print ("set logging level failed ,the level is invalid.")

    def create_push(self):
        """Create a Push notification."""
        return Push(self)

    def create_device(self):
        """Create a Device information."""
        return Device(self)

    def create_report(self):
        """Create a Report."""
        return Report(self)

    def create_schedule(self):
        """Create a Schedule."""
        return Schedule(self)

class GroupPush(JPush):

    def __init__(self, key, secret):
        super().__init__('group-' + key, secret)

    def create_push(self):
        """Create a Group Push notification."""
        return Push(self, url = common.GROUP_PUSH_URL)
