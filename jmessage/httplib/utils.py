#!/usr/bin/env python
# coding: utf8


class ParamsReader:
    """ 当为PUT方法时使用

    :param fp: StringIO实例
    """
    def __init__(self, fp):
        self.fp = fp

    def read(self, size):
        """当PUT请求时，供PycURL使用

        :param size: int, 读取大小
        """
        return self.fp.read(size)
