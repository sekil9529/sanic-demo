# coding: utf-8

from .sqlalchemy import SQLAlchemyMiddleware
from .timer import TimerMiddleware

MIDDLEWARE_TUPLE = (
    SQLAlchemyMiddleware,
    TimerMiddleware,
)
