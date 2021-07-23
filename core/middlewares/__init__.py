# coding: utf-8

from .sqlalchemy import SQLAlchemyMiddleware

MIDDLEWARE_TUPLE = (
    SQLAlchemyMiddleware,
)
