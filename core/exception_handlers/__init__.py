# coding: utf-8

from __future__ import annotations

from .base import BaseExcHandler
from .error_code import ErrorCodeExcHandler
from .unknown import UnknownExcHandler

# 注意：UnknownExcHandler要放在最后
EXC_HDL_TUPLE: tuple[type[BaseExcHandler], ...] = (
    ErrorCodeExcHandler,
    UnknownExcHandler,
)
