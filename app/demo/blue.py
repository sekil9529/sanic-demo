# coding: utf-8

"""demo蓝图"""

from sanic import Blueprint
from .views import hello, HelloView, error, unknown_error
from .views import redis_test


bp: Blueprint = Blueprint('demo', url_prefix='demo')


bp.add_route(hello, "/hello", ('GET',))
bp.add_route(HelloView.as_view(), "/hello/cbv")
bp.add_route(error, "/error", ('GET',))
bp.add_route(unknown_error, "/error/unknown", ('GET',))

bp.add_route(redis_test, "redis/test", ("GET",))
