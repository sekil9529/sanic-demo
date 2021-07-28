# coding: utf-8

from sanic import Request, HTTPResponse

from .base import BaseMiddleware


class SQLAlchemyMiddleware(BaseMiddleware):
    """SQLAlchemy中间件"""

    async def before_request(self, request: Request) -> None:
        """request绑定db_session"""
        request.ctx.db_session = self._app.ctx.DBSession()

    async def before_response(self, request: Request, response: HTTPResponse) -> None:
        """确保db_session放回连接池"""
        if hasattr(request.ctx, 'db_session'):
            await request.ctx.db_session.close()
