# coding: utf-8

from asyncio.base_events import BaseEventLoop

from sanic import Sanic
from aioredis import from_url
from aioredis.client import Redis

from .base import BaseListener
from libs.logger import LoggerProxy

logger = LoggerProxy(__name__)


class RedisListener(BaseListener):
    """Redis监听"""

    config_name: str = "REDIS"

    async def after_server_start(self, app: Sanic, loop: BaseEventLoop) -> None:
        """app绑定Redis"""
        redis_url: str = app.config.get(self.config_name)
        redis_client: Redis = await from_url(redis_url)
        self.ext.redis_client = app.ctx.redis_client = redis_client
        logger.info("Redis bound.")

    async def before_server_stop(self, app: Sanic, loop: BaseEventLoop) -> None:
        """释放连接"""
        await self.ext.redis_client.close()
        logger.info("Redis closed.")
