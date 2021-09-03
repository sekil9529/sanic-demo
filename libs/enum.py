# coding: utf-8

from __future__ import annotations
from collections.abc import Sequence
from enum import Enum, unique


def index_value_unique(indexes: Sequence[int]):
    """装饰器：枚举成员的某个下标元素唯一"""

    def wrapper(enumeration: type[Enum]):
        enumeration = unique(enumeration)
        for index in indexes:
            number_set = set()
            for elem in enumeration:
                index_value = elem.value[index]
                if index_value in number_set:
                    raise ValueError('duplicate value found in %r, index [%d]' % (elem, index))
                number_set.add(index_value)
        return enumeration
    return wrapper


def first_value_unique(enumeration):
    """装饰器：枚举成员的第一个元素唯一"""
    return index_value_unique((0,))(enumeration)


def keyword_value_unique(keywords: Sequence[str]):
    """装饰器：枚举成员的某个关键字唯一"""
    def wrapper(enumeration: type[Enum]):
        enumeration = unique(enumeration)
        for keyword in keywords:
            number_set = set()
            for elem in enumeration:
                index_value = getattr(elem.value, keyword)
                if index_value in number_set:
                    raise ValueError('duplicate value found in %r, keyword `%s`' % (elem, keyword))
                number_set.add(index_value)
        return enumeration
    return wrapper
