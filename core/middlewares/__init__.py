# coding: utf-8

from __future__ import annotations

from .base import BaseMiddleware
from .sqlalchemy import SQLAlchemyMiddleware
from .timer import TimerMiddleware

MIDDLEWARE_TUPLE: tuple[type[BaseMiddleware], ...] = (
    SQLAlchemyMiddleware,
    TimerMiddleware,
)
