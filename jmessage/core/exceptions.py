#!/usr/bin/env python
# coding: utf8


class ParamsError(Exception):
    """参数错误异常
    """
    pass


class SDKRespError(Exception):
    """SDK异常基类

    :param resp: httplib.HTTPResponse 实例
    :param message: 可选参数, 自定义异常消息
    """
    def __init__(self, resp, message=None):
        self.resp = resp
        self.message = message

    def __str__(self):
        message = "Error Code: {0}, message: {1}.\
                ".format(self.resp.status_code, self.resp.content)
        if self.message:
            message += self.message

        return message


class SDKClientError(SDKRespError):
    """4xx SDK HTTP Error
    """
    pass


class BadRequest(SDKClientError):
    """400 Bad Request
    """
    pass


class Unauthorized(SDKClientError):
    """401 Unauthorized
    """
    pass


class Forbidden(SDKClientError):
    """403 Forbidden
    """
    pass


class NotFound(SDKClientError):
    """404 NotFound
    """
    pass


class MethodNotAllowed(SDKClientError):
    """405 Method Not Allowed
    """
    pass


class SDKServerError(SDKRespError):
    """5xx SDK Server Error
    """
    pass
