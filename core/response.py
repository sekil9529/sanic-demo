# coding: utf-8

"""响应相关配置"""

from __future__ import annotations
from typing import Any, Optional
from decimal import Decimal
from json import JSONEncoder, dumps
from datetime import datetime
from sanic import json
from sanic.response import HTTPResponse

from .error_code import ECEnum


class ExtJsonEncoder(JSONEncoder):
    """扩展json编码器"""
    def default(self, o: Any) -> Any:
        if isinstance(o, datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(o, Decimal):
            return str(o)
        return super().default(o)


def response_ok(data: Any = None) -> HTTPResponse:
    """成功返回

    :param data: 数据
    :return:
    """
    # 错误码
    code: str = "0"
    # 内容
    content: dict[str, Any] = dict(code=code, data=data)
    return json(content, dumps=dumps, cls=ExtJsonEncoder)


def response_fail(
        enum: Optional[ECEnum] = None,
        desc: Any = "") -> HTTPResponse:
    """失败返回

    :param enum: 错误码枚举类
    :param desc: 错误详情
    :return:
    """
    if enum is None:
        enum = ECEnum.ServerError
    # 错误码
    code: str = str(enum.code)
    # error码
    error: str = enum.error
    # 错误信息
    message: str = enum.message
    # 内容
    content: dict[str, Any] = dict(code=code, error=error, message=message, desc=desc)
    return json(content, dumps=dumps, cls=ExtJsonEncoder)
