import json
import logging
import warnings
import base64
import requests
from hyper import HTTP20Connection
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

    def _request(self, method, body, url,base_url=None):
        headers = {}
        headers['user-agent'] = 'jpush-api-python-client'
        headers['connection'] = 'keep-alive'
        headers['content-type'] = 'application/json;charset:utf-8'

        logger.debug("Making %s request to %s. Headers:\n\t%s\nBody:\n\t%s",
                     method, url, '\n\t'.join('%s: %s' % (key, value) for (key, value) in headers.items()), body)
        base64string = base64.encodestring('%s:%s' % (self.key, self.secret))[:-1]
        authheader = "Basic %s" % base64string
        headers['Authorization'] = authheader
        conn = HTTP20Connection(host=base_url, secure=True)

        response = conn.request(method,url,headers=headers,body=body)
        resp = conn.get_response(response)
        #add status_code to test
        resp.status_code=resp.status
        logger.debug(resp.status)
        logger.debug(resp.read())
        return resp

    def push(self, payload):
        """Push this payload to the specified recipients.

        Payload: a dictionary the contents to send, e.g.:
            {'aps': {'alert': 'Hello'}, 'android': {'alert': 'Hello'}}
        """
        body = json.dumps(payload)
        self._request('POST', body, common.PUSH_URL, common.PUSH_BASEURL)

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