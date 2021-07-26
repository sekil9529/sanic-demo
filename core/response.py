# coding: utf-8

"""响应相关配置"""

from typing import Any, Dict, Optional
from decimal import Decimal
from json import JSONEncoder
from datetime import datetime
from sanic import json
from sanic.response import HTTPResponse

from .error_code import ECEnum
from libs.datetime import to_unix_timestamp


class ExtJsonEncoder(JSONEncoder):
    """扩展json编码器"""
    def default(self, o: Any) -> Any:
        if isinstance(o, datetime):
            return to_unix_timestamp(o)
        elif isinstance(o, Decimal):
            return str(o)
        return super().default(o)


def response_ok(data: Any = None) -> HTTPResponse:
    """成功返回

    :param data: 数据
    :return:
    """
    # 错误码
    code: str = '0'
    # 内容
    content: Dict[str, Any] = dict(code=code, data=data)
    return json(content, cls=ExtJsonEncoder)


def response_fail(
        enum: Optional[ECEnum] = None,
        desc: Any = '') -> HTTPResponse:
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
    content: Dict[str, Any] = dict(code=code, error=error, message=message, desc=desc)
    # 响应状态码
    status_code = 500 if code == '500' else 200
    return json(content, cls=ExtJsonEncoder, status=status_code)
