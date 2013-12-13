# -*- coding: utf-8 -*-
#
# Report Received API
#

import httplib

API_HOST = "report.jpush.cn"
API_PATH = "/v2/received"


class RecvClient:
    """ JPush Report Received Python Client Class"""
    def __init__(self, appkey, master_secret, timeout=5):
        self._timeout = timeout
        self._auth = ("%s:%s" % (appkey, master_secret)).encode("base64").strip()
        self._conn = None
        self._reconnect()

    def _reconnect(self):
        if self._conn is None:
            self._conn = httplib.HTTPSConnection(API_HOST,
                                                 timeout=self._timeout)

    def close(self):
        """close connection"""
        if self._conn:
            self._conn.close()

    def __del__(self):
        try:
            self.close()
        except:
            pass

    def get_recv(self, msg_ids):
        """get recv result"""
        if isinstance(msg_ids, list):
            msg_ids = [str(i) for i in msg_ids]
            msg_ids = ",".join(msg_ids)

        url = "%s?msg_ids=%s" % (API_PATH, msg_ids)
        auth_header = {"Authorization": "Basic %s" % self._auth}

        if self._conn is None:
            self._reconnect()

        try:
            self._conn.request(method="GET", url=url, headers=auth_header)
            print self._conn.getresponse().read()
        except Exception, e:
            self._conn = None
            print "Request receive result error: %s" % e
