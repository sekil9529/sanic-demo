# coding: utf-8

# from contextvars import ContextVar

from .base import BaseMiddleware

# _DB_SESSION_VAR = ContextVar('db session')


class SQLAlchemyMiddleware(BaseMiddleware):
    """SQLAlchemy中间件"""

    async def before_request(self, request) -> None:
        """request绑定db_session"""
        request.ctx.db_session = self._app.ctx.DBSession()
        # request.ctx.db_session_token = _DB_SESSION_VAR.set(request.ctx.db_session)

    async def before_response(self, request, response) -> None:
        """确保db_session放回连接池"""
        # if hasattr(request.ctx, 'db_session_token'):
        if hasattr(request.ctx, 'db_session'):
            # _DB_SESSION_VAR.reset(request.ctx.db_session_token)
            await request.ctx.db_session.close()
