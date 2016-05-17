import json
import logging
from jpush import common

logger = logging.getLogger('jpush')


class Schedule(object):
    """JPush Report API V3"""
    def __init__(self, jpush):
        self._jpush = jpush

    def send(self, method, url, body, content_type=None, version=3):
        response = self._jpush._request(method, body, url, content_type, version=3)
        return ScheduleResponse(response)

    def post_schedule(self, schedulepayload):
        url=common.BASE_SCHEDULEURL
        body = json.dumps(schedulepayload)
        result = self.send("POST", url, body)
        return result

    def get_schedule_by_id(self, schedule_id):
        url=common.BASE_SCHEDULEURL + schedule_id
        body = None
        result = self.send("GET", url, body)
        return result

    def get_schedule_list(self, page_id):
        if page_id is not None:
            url=common.BASE_LISTURL + page_id
        else:
            url = common.BASE_LISTURL
        body = None
        result = self.send("GET", url, body)
        return result

    def put_schedule(self, schedulepayload, schedule_id):
        url = common.BASE_SCHEDULEURL + schedule_id
        body = json.dumps(schedulepayload)
        result = self.send("PUT", url, body)
        return result

    def delete_schedule(self,schedule_id):
        url = common.BASE_SCHEDULEURL + schedule_id
        body = None
        result = self.send("DELETE", url, body)
        return result


class ScheduleResponse(object):
    """Response to a successful device request send.

    Right now this is a fairly simple wrapper around the json payload response,
    but making it an object gives us some flexibility to add functionality
    later.

    """
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
        return "Schedule response Payload: {0}".format(self.payload)