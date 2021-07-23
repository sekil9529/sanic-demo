# coding: utf-8

"""错误码枚举类"""

from enum import Enum, unique
from types import DynamicClassAttribute


def first_value_unique(enumeration):
    """ 装饰器：序列的第一个元素唯一 """
    unique(enumeration)
    number_set = set()
    for elem in enumeration:
        first_value = elem.value[0]
        if first_value in number_set:
            raise ValueError('duplicate first value found in %r' % elem)
        number_set.add(first_value)
    return enumeration


class BaseECEnum(Enum):
    """错误码基类

    定义方式：error = (code, message)
    """

    @DynamicClassAttribute
    def code(self):
        """错误码"""
        return self.value[0]

    @DynamicClassAttribute
    def message(self):
        """错误信息"""
        return self.value[1]

    @DynamicClassAttribute
    def error(self):
        """error码"""
        return self.name
