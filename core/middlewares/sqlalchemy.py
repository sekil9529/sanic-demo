# coding: utf-8

from contextvars import ContextVar

from .base import BaseMiddleware


class SQLAlchemyMiddleware(BaseMiddleware):
    """SQLAlchemy中间件"""

    _db_session_var = ContextVar('db session')

    async def before_request(self, request):
        """request绑定db_session"""
        request.ctx.db_session = self._app.ctx.DBSession()
        request.ctx.db_session_token = self._db_session_var.set(request.ctx.db_session)

    async def before_response(self, request, response):
        """确保db_session放回连接池"""
        if hasattr(request.ctx, 'db_session_token'):
            self._db_session_var.reset(request.ctx.db_session_token)
            await request.ctx.db_session.close()
