# coding: utf-8

import logging
from typing import Type
from sanic import HTTPResponse
from sanic.request import Request

from .base import BaseExcHandler
from core.response import response_fail

log = logging.getLogger()


class UnknownExcHandler(BaseExcHandler):
    """未知异常处理"""

    def get_exception(self) -> Type[Exception]:
        return Exception

    def handle(self, request: Request, exception: Exception) -> HTTPResponse:
        log.exception(exception)
        return response_fail()
