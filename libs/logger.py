# coding: utf-8

from __future__ import annotations
import logging
from typing import Optional, Any


class LoggerProxy:
    """logger代理"""

    __slots__: tuple[str, ...] = ('_name', '_logger')

    def __init__(self, name: Optional[str] = None) -> None:
        self._name: Optional[str] = name
        self._logger: Optional['logging.Logger'] = None

    def _ensure_logger(self) -> None:
        """确保logger初始化"""
        if self._logger is None:
            self._logger = logging.getLogger(self._name)

    def __getattr__(self, item) -> Any:
        self._ensure_logger()
        return getattr(self._logger, item)
