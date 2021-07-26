# coding: utf-8

"""demo蓝图"""

from sanic import Blueprint
from .views import hello, HelloView, error, unknown_error


bp = Blueprint('demo', url_prefix='demo')


bp.add_route(hello, "/hello", ('GET',))
bp.add_route(HelloView.as_view(), "/hello/cbv")
bp.add_route(error, "/error", ('GET',))
bp.add_route(unknown_error, "/error/unknown", ('GET',))
