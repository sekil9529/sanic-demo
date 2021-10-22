# coding: utf-8

from __future__ import annotations
import abc
from types import SimpleNamespace
from asyncio.base_events import BaseEventLoop
from sanic import Sanic

from settings.base import BaseSettings


class BaseListener(metaclass=abc.ABCMeta):
    """监听基类
    ASGI 模式下
    main_process_start 与 main_process_stop 会被忽略
    before_server_start 与 after_server_stop 定义不明确
    因此这里只推荐使用 after_server_start，before_server_stop

    main_process_start and main_process_stop will be ignored
    before_server_start will run as early as it can, and will be before after_server_start, but technically, the server is already running at that point
    after_server_stop will run as late as it can, and will be after before_server_stop, but technically, the server is still running at that point
    """

    __slots__ = ('_settings', 'ctx')

    def __init__(self, settings: type[BaseSettings]) -> None:
        """赋初值

        :param settings: 配置类
        """
        self._settings = settings
        self.ctx: SimpleNamespace = SimpleNamespace()  # 扩展

    @abc.abstractmethod
    async def after_server_start(self, app: Sanic, loop: BaseEventLoop) -> None:
        pass

    @abc.abstractmethod
    async def before_server_stop(self, app: Sanic, loop: BaseEventLoop) -> None:
        pass

