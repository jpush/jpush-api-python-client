#!/usr/bin/env python
# coding: utf8
"""
Exceptions for HTTPClient
"""


class HeaderError(Exception):
    """Exception raise when header is not dict type
    """
    pass


class ParamsError(Exception):
    """Exception raise when http param is error
    """
    pass


class ParseRespError(Exception):
    """Exception raise when response parse not right
    """
    pass


class CurlError(Exception):
    """Exception raise when error occur during using pycurl

    :param code: HTTP error integer error code
    :param message: error message string
    """
    def __init__(self, code, message=None):
        self.code = code
        message = message or responses.get(code, "Unknown")
        Exception.__init__(self, "%d: %s" % (self.code, message))
