# coding: utf-8

from __future__ import annotations

from typing import Any

from sanic import Request
from sanic.response import json, HTTPResponse
from sanic.views import HTTPMethodView
from aioredis.client import Redis

from core.response import response_ok


async def hello(request: Request) -> HTTPResponse:
    """hello word"""
    # return json({'message': 'hello world!'})
    return response_ok({'message': 'hello world!'})


class HelloView(HTTPMethodView):
    """cbv"""

    async def get(self, request: Request) -> HTTPResponse:
        return json({'message': 'hello world!'})


async def error(request: Request) -> HTTPResponse:
    """测试错误码异常"""
    from core.error_code import ECEnum
    from libs.error_code.exception import ECException
    raise ECException(ECEnum.TestError)


async def unknown_error(request: Request) -> HTTPResponse:
    """测试未知异常"""
    raise


async def redis_test(request: Request) -> HTTPResponse:
    """测试redis"""
    redis_client: Redis = request.ctx.redis_client
    key: str = "num"
    num: int = await redis_client.incr(key)
    await redis_client.expire(key, 30)
    data: dict[str, Any] = {
        "num": num
    }
    return response_ok(data)
