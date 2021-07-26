# coding: utf-8

from .error_code import ErrorCodeExcHandler
from .unknown import UnknownExcHandler

# 注意：UnknownExcHandler要放在最后
EXC_HDL_TUPLE = (
    ErrorCodeExcHandler,
    UnknownExcHandler,
)
