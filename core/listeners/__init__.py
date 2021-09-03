# coding: utf-8

from __future__ import annotations

from .base import BaseListener
from .sqlalchemy import SQLAlchemyListener

LISTENER_TUPLE: tuple[type[BaseListener], ...] = (
    SQLAlchemyListener,
)
