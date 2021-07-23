# coding: utf-8

from sanic import Blueprint
from .views import user_list


bp = Blueprint('user', url_prefix='user')


bp.add_route(user_list, "/list", ('GET',))  # 用户列表
