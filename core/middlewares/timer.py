# coding: utf-8

import time
import logging
from contextvars import ContextVar

from sanic import Request, HTTPResponse

from .base import BaseMiddleware

log = logging.getLogger()


_TIME_VAR: ContextVar = ContextVar('time')


class TimerMiddleware(BaseMiddleware):
    """计时中间件"""

    threshold: float = 1.0
    token_key: str = 'time_token'

    async def before_request(self, request: Request) -> None:
        setattr(request.ctx, self.token_key, _TIME_VAR.set(time.time()))

    async def before_response(self, request: Request, response: HTTPResponse) -> None:
        diff = time.time() - _TIME_VAR.get()
        if diff > self.threshold:
            log.warning('%s, response timeout: %.6f' % (request.name, diff))
        if hasattr(request.ctx, self.token_key):
            _TIME_VAR.reset(getattr(request.ctx, self.token_key))
