# coding: utf-8

from __future__ import annotations

from typing import Optional, Any
from configparser import RawConfigParser as ConfigParser


class Config:
    """配置文件解析"""

    __slots__ = ('_section', '_cnf')

    def __init__(self, file_path: str, section: Optional[str] = None, encoding: str = 'utf-8') -> None:
        self._section = section
        self._cnf = ConfigParser()
        self._cnf.read(file_path, encoding=encoding)

    def format(self) -> dict[str, Any]:
        """格式化"""
        if self._section is None:
            return {section: dict(self._cnf.items(section)) for section in self._cnf.sections()}
        else:
            return dict(self._cnf.items(self._section))
