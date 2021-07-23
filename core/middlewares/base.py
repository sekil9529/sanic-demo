# coding: utf-8

import abc

from sanic import Sanic


class BaseMiddleware(metaclass=abc.ABCMeta):
    """中间件基类"""

    __slots__ = ('_app',)

    def __init__(self, app: Sanic) -> None:
        """赋初值

        :param app: sanic app
        """
        self._app = app

    @abc.abstractmethod
    async def before_request(self, request) -> None:
        """请求前处理"""
        pass

    @abc.abstractmethod
    async def before_response(self, request, response) -> None:
        """响应前处理"""
        pass
