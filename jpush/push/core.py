import json
import logging

from jpush import common

logger = logging.getLogger('jpush')

class Push(object):
    """A push notification. Set audience, message, etc, and send."""

    def __init__(self, jpush):
        self._jpush = jpush
        self.audience = None
        self.notification = None
        self.platform = None
        self.options = None
        self.message = None

    @property
    def payload(self):
        data = {
            "audience": self.audience,
            "platform": self.platform,
        }
        if (self.notification is None) and (self.message is None):
            raise ValueError("Notification and message cannot be both empty")
        if self.notification is not None:
            data['notification'] = self.notification
        if self.options is not None:
            data['options'] = self.options
        if self.message is not None:
            data['message'] = self.message
        return data

    def send(self):
        """Send the notification.

        :returns: :py:class:`PushResponse` object with ``push_ids`` and
            other response data.
        :raises JPushFailure: Request failed.
        :raises Unauthorized: Authentication failed.

        """
        body = json.dumps(self.payload)
        response = self._jpush._request('POST', body,
            common.PUSH_URL, 'application/json', version=3)

        print (response.content) 
        return PushResponse(response)

    def send_validate(self):
        """Send the notification to validate.

        :returns: :py:class:`PushResponse` object with ``push_ids`` and
            other response data.
        :raises JPushFailure: Request failed.
        :raises Unauthorized: Authentication failed.

        """
        body = json.dumps(self.payload)
        response = self._jpush._request('POST', body,
            common.VALIDATE_PUSH_URL, 'application/json', version=3)

        print (response.content) 
        return PushResponse(response)


class PushResponse(object):
    """Response to a successful push notification send.

    Right now this is a fairly simple wrapper around the json payload response,
    but making it an object gives us some flexibility to add functionality
    later.

    """
    payload = None

    def __init__(self, response):
        data = response.json()
        self.payload = data

    def __str__(self):
        return "Response Payload: {0}".format(self.payload)
