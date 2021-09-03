# coding: utf-8

from __future__ import annotations

from sanic import HTTPResponse
from sanic.request import Request

from .base import BaseExcHandler
from libs.error_code.exception import ECException
from core.response import response_fail


class ErrorCodeExcHandler(BaseExcHandler):
    """错误码异常处理"""

    def get_exception(self) -> type[ECException]:
        return ECException

    def handle(self, request: Request, exception: ECException) -> HTTPResponse:
        return response_fail(enum=exception.enum)
