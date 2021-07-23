# coding: utf-8


class ECException(Exception):
    """错误码异常类"""

    __slots__ = ('enum',)

    def __init__(self, enum):
        self.enum = enum
