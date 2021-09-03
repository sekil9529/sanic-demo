# coding: utf-8

from sanic.response import json, HTTPResponse
from sanic.views import HTTPMethodView

from core.response import response_ok


async def hello(request) -> HTTPResponse:
    """hello word"""
    # return json({'message': 'hello world!'})
    return response_ok({'message': 'hello world!'})


class HelloView(HTTPMethodView):
    """cbv"""

    async def get(self, request) -> HTTPResponse:
        return json({'message': 'hello world!'})


async def error(request) -> HTTPResponse:
    """测试错误码异常"""
    from core.error_code import ECEnum
    from libs.error_code.exception import ECException
    raise ECException(ECEnum.TestError)


async def unknown_error(request):
    """测试未知异常"""
    raise
