# coding: utf-8

from __future__ import annotations

from sanic import HTTPResponse
from sanic.request import Request

from libs.logger import LoggerProxy
from .base import BaseExcHandler
from core.response import response_fail

logger: LoggerProxy = LoggerProxy(__name__)


class UnknownExcHandler(BaseExcHandler):
    """未知异常处理"""

    def get_exception(self) -> type[Exception]:
        return Exception

    def handle(self, request: Request, exception: Exception) -> HTTPResponse:
        logger.exception(exception)
        return response_fail()
