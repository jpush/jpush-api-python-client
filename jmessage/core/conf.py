"""
URL Templates for JMessage

__author__ = "admin@readthecodes.com"
"""

# Base API URL
BASE_URL = 'https://api.im.jpush.cn'

# Messages
SEND_MESSAGE = '/messages?resend={is_resend}'
GET_MEDIA_TOKEN = '/upload_token/?provider={provider}&\
        file_type={file_type}&resource_id={resource_id}'

# Users
REGISTER_USER = '/users/'
REGISTER_ADMIN = '/admins/'
GET_USER_INFO = '/users/{username}/'
UPDATE_USER_PASSWORD = '/users/{username}/password'
UPDATE_USER_INFO = '/user/{username}'
GET_USER_LIST = '/users?start={start}&count={count}'
DEL_USER = '/users/{username}/'

# Groups
GET_USER_GROUPS = '/users/{username}/groups/'
GET_GROUP_INFO = '/group/{gid}/'
GET_GROUP_MEMBER_LIST = '/groups/{gid}/members'
GET_APP_GROUPS = '/groups?start={start}&count={count}'
CREATE_GROUP = '/groups'
UPDATE_GROUP_MEMBERS = '/groups/{gid}/members'
UPDATE_GROUP_INFO = '/groups/{gid}'
DEL_GROUP = '/groups/{gid}'

# Friends
GET_FRIEND_LIST = '/users/{username}/friends'
GET_FRIEND_INFO = '/users/{username}/friends/{friend_username}'
BATCH_GET_FRIEND_INFO = '/users/{username}/friends_batch'
ADD_FRIEND = '/users/{username}/friends/{friend_username}'
DEL_FRIEND = '/users/{username}/friends/{friend_username}'
UPDATE_FRIEND_NOTENAME = '/users/{username}\
        /friends/{friend_username}/'
