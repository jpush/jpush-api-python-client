import logging
from jpush import common

logger = logging.getLogger('jpush')


class Report(object):
    """JPush Report API V3"""
    def __init__(self, jpush):
        self._jpush = jpush

    def send(self, method, body,url,base_url=None):
        """Send the request
        """
        response = self._jpush._request(method, body,url,common.REPORT_BASEURL)
        return response

    def get_received(self,msg_ids):
        url=common.RECEIVED_URL+msg_ids
        body = None
        received = self.send("GET", body, url ,common.REPORT_BASEURL)
        return received

    def get_messages(self, msg_ids):
        url = common.MESSAGES_URL + msg_ids
        body = None
        messages = self.send("GET", body, url, common.REPORT_BASEURL)
        return messages

    def get_users(self, time_unit,start,duration):
        url = common.USERS_URL + "time_unit="+time_unit+"&start="+start+"&duration="+duration
        body = None
        users = self.send("GET", body, url, common.REPORT_BASEURL)
        return users


class ReportResponse(object):

    payload = None
    status_code = None

    def __init__(self, response):
        self.status_code = response.status_code
        if 0 != len(response.content):
            data = response.json()
            self.payload = data
        elif 200 == response.status_code:
            self.payload = "success"

    def get_status_code(self):
        return self.status_code

    def __str__(self):
        return "Report response Payload: {0}".format(self.payload)