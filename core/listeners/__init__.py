# coding: utf-8

from __future__ import annotations

from .base import BaseListener
from .redis import RedisListener


LISTENER_TUPLE: tuple[type[BaseListener], ...] = (
    RedisListener,
)
