import json
import logging


BASE_URL = "https://api.jpush.cn/"
PUSH_URL = BASE_URL + 'v3/push'
VALIDATE_PUSH_URL = BASE_URL + 'v3/push/validate'

DEVICE_BASEURL = "https://device.jpush.cn/"
DEVICE_URL = DEVICE_BASEURL + "v3/devices/"
TAG_URL = DEVICE_BASEURL + "v3/tags/"
TAGLIST_URL = TAG_URL
ALIAS_URL = DEVICE_BASEURL + "v3/aliases/"

logger = logging.getLogger('jpush')

class Unauthorized(Exception):
    """Raised when we get a 401 from the server"""


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
        super(JPushFailure, self).__init__(*args)

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

        return cls(error, error_code, details, response, response.status_code,
            response.content)
