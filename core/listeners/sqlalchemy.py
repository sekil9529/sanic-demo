# coding: utf-8

from asyncio.base_events import BaseEventLoop

from sanic import Sanic
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from .base import BaseListener


class SQLAlchemyListener(BaseListener):
    """SQLAlchemy监听"""

    async def after_server_start(self, app: Sanic, loop: BaseEventLoop) -> None:
        """app绑定DBSession"""
        self.ext.engine = create_async_engine(self._settings.SQLALCHEMY_DATABASE_URL, echo=False,
                                              **self._settings.SQLALCHEMY_ENGINE_OPTIONS)
        app.ctx.DBSession = sessionmaker(self.ext.engine, expire_on_commit=False, class_=AsyncSession)

    async def before_server_stop(self, app: Sanic, loop: BaseEventLoop) -> None:
        """释放连接池"""
        await self.ext.engine.dispose()
