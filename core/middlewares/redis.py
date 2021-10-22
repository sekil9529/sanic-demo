# coding: utf-8

from sanic import Request, HTTPResponse

from .base import BaseMiddleware


class RedisMiddleware(BaseMiddleware):
    """Redis中间件"""

    async def before_request(self, request: Request) -> None:
        """request绑定redis client"""
        request.ctx.redis_client = self._app.ctx.redis_client

    async def before_response(self, request: Request, response: HTTPResponse) -> None:
        """redis_client自动放回连接池，无须处理"""
        pass
