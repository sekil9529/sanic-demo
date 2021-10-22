# coding: utf-8

import abc

from sanic import Sanic, Request, HTTPResponse


class BaseMiddleware(metaclass=abc.ABCMeta):
    """中间件基类"""

    __slots__ = ()

    @abc.abstractmethod
    async def before_request(self, request: Request) -> None:
        """请求前处理"""
        pass

    @abc.abstractmethod
    async def before_response(self, request: Request, response: HTTPResponse) -> None:
        """响应前处理"""
        pass
