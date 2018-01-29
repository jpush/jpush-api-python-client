import json
import logging
import requests

PUSH_URL    = 'https://api.jpush.cn/v3/'
REPORT_URL  = 'https://report.jpush.cn/v3/'
DEVICE_URL  = 'https://device.jpush.cn/v3/devices/'
ALIAS_URL   = 'https://device.jpush.cn/v3/aliases/'
TAG_URL     ='https://device.jpush.cn/v3/tags/'
SCHEDULE_URL = 'https://api.jpush.cn/v3/schedules/'
ADMIN_URL   ='https://admin.jpush.cn/v1/'

logger = logging.getLogger('jpush')


class Unauthorized(Exception):
    """Raised when we get a 401 from the server"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class JPushFailure(Exception):
    """Raised when we get an error response from the server.
    :param args: For backwards compatibility, ``*args`` includes the status and
        response body.
    """

    error = None
    error_code = None
    details = None
    response = None

    def __init__(self, error, error_code, details, response, *args):
        self.error = error
        self.error_code = error_code
        self.details = details
        self.response = response
        # super(self, JPushFailure).__init__(*args)

    @classmethod
    def from_response(cls, response):
        """Instantiate a ValidationFailure from a Response object"""
        try:
            payload = response.json()
            error = payload.get('error')
            error_code = error.get('code')
            details = error.get('message')
        except ValueError:
            error = response.reason
            error_code = None
            details = response.content

        logger.error(
            "Request failed with status %d: '%s %s': %s",
            response.status_code, error_code, error, json.dumps(details))

        return cls(error, error_code, details, response, response.status_code, response.content)

    def __str__(self):
        return repr(self.response.content)


class APIConnectionException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class APIRequestException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


































