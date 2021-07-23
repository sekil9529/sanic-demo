# coding: utf-8

from sanic import Blueprint
from .views import hello, HelloView


bp = Blueprint('demo', url_prefix='demo')


bp.add_route(hello, "/hello", ('GET',))
bp.add_route(HelloView.as_view(), "/hello/cbv")
