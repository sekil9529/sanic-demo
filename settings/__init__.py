# coding: utf-8

from __future__ import annotations

from enum import Enum, unique
from typing import Optional

from .base import BaseSettings
from .development import Settings as DevSettings
from .production import Settings as ProSettings


@unique
class EnvEnum(Enum):
    """环境枚举类"""
    DEV: type[BaseSettings] = DevSettings
    PRO: type[BaseSettings] = ProSettings


def get_settings(env: Optional[str] = None) -> type[BaseSettings]:
    """获取配置"""
    if env is None:
        env = 'DEV'
    settings = getattr(EnvEnum, env.upper()).value
    return settings
