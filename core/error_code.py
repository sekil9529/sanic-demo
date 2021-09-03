# coding: utf-8

from libs.error_code.enum import BaseECEnum, ECData


class ECEnum(BaseECEnum):
    """错误码枚举类"""
    ServerError = ECData("500", "服务异常，请稍后重试")

    TestError = ECData("TEST", "测试错误")
