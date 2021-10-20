# coding: utf-8

from __future__ import annotations

from .base import BaseMiddleware
from .timer import TimerMiddleware

MIDDLEWARE_TUPLE: tuple[type[BaseMiddleware], ...] = (
    TimerMiddleware,
)
