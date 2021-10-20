# coding: utf-8

from __future__ import annotations

from typing import NamedTuple
from enum import EnumMeta, Enum, unique
from types import DynamicClassAttribute

__all__ = (
    "ECData",
    "BaseECEnum"
)


class ECData(NamedTuple):
    """错误码数据"""

    # 错误码
    code: str
    # 错误信息
    message: str = "服务器异常"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ECData):
            raise NotImplemented
        return self.code == other.code


class _ECEnumMeta(EnumMeta):
    """错误码枚举元类"""

    def __new__(mcs, *args, **kwargs):
        enum_class = super(_ECEnumMeta, mcs).__new__(mcs, *args, **kwargs)
        # 唯一
        return unique(enum_class)


class BaseECEnum(Enum, metaclass=_ECEnumMeta):
    """错误码基类"""

    @DynamicClassAttribute
    def code(self):
        """错误码"""
        return self.value.code

    @DynamicClassAttribute
    def message(self):
        """错误信息"""
        return self.value.message

    @DynamicClassAttribute
    def error(self):
        """error码"""
        return self.name
