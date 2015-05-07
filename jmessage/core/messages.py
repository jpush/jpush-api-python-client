#!/usr/bin/env python
# coding: utf8
from __future__ import absolute_import

from types import ListType

from jmessage.core import conf
from jmessage.core.base import BaseSDK
from jmessage.core.exceptions import ParamsError


class Messages(BaseSDK):
    """消息相关API

    :param appKey: string, 应用的AppKey
    :param masterSecret: string, 相应的masterSecret
    """
    def __init__(self, appKey, masterSecret):
        super(Messages, self).__init__(appKey, masterSecret)

    def send_messages(self, version, target_type, target_id,
                      from_type, from_id, from_platform,
                      create_time, msg_type, msg_body,
                      from_name=None, target_name=None, is_resend='false'):
        """发送消息

        :param version: int, 协议版本号。第一版本：1，以此类推。
        :param target_type: string, 接收者类型, 包含：single, group
        :param target_id: int, 接收者ID, 可能为username或group_id
        :param from_type: string, 发送者类型, 可能值为: user, robot, admin
        :param from_id: int, 发送者 username
        :param from_platform: string, 发送者平台。可选值：
                              a--Android
                              i--iOS
                              w--WinPhone
                              web--Web
                              api--API
        :param create_time: int, 消息发送时间戳
        :param msg_type: string, 消息类型。可选值：
                              text--文本
                              image--图片
                              voice--声音
                              location--地理位置
                              custom--自定义消息
        :param msg_body: dict, 消息体, 不同的消息类型有不同的消息体
        :param from_name: string, 发送者展示名, 可选
        :param target_name: string, 接收者的展示名, 可选
        """
        pass

    def get_media_token(self, provider, file_type, resource_id,
                        file_blocks=None, file_hash=None, file_size=None):
        """获取上传媒体文件的密钥

        :param provider: string, 云存储提供商，可选值为：qiniu, upyun
        :param file_type: string, 文件类型
        :param resource_id: string, 资源编码
        :param file_blocks: int, 可选, provider 为 upyun 时需要。
        :param file_hash: string, 可选, provider 为 upyun 时需要。
        :param file_size: int, 可选, provider 为 upyun 时需要。
        """
        pass
