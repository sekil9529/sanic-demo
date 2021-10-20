# coding: utf-8

from __future__ import annotations

from .base import BaseSettings, CONFIG_INFO


class Settings(BaseSettings):
    """配置类"""

    DEBUG: bool = False

    SECRET_KEY: str = 'wdATN(TPpSB-269m0Ayd9[H+^:/TZW;qkIJD8a:-K{'

    ACCESS_LOG: bool = False

    # 跨域相关
    ENABLE_CORS: bool = True
    CORS_SUPPORTS_CREDENTIALS: bool = True

    # tortoise
    TORTOISE: dict = {
        "connections": {
            "default": {
                "engine": "tortoise.backends.mysql",
                "credentials": {
                    "host": CONFIG_INFO["db"]["host"],
                    "port": CONFIG_INFO["db"]["port"],
                    "user": CONFIG_INFO["db"]["user"],
                    "password": CONFIG_INFO["db"]["password"],
                    "database": CONFIG_INFO["db"]["database"],
                    "maxsize": 15,
                    # 注意：启动时直接创建5个session
                    "minsize": 15,
                    # 回收时间，每次获取session时判断，如果超时，全部重新创建
                    "pool_recycle": 60 * 60 * 2,
                    # 设置事务隔离级别为RC
                    "init_command": "SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED",
                }
            }
        },
        "apps": {
            "models": {
                "models": ["app.models"],
                "default_connection": "default",
            }
        },
        "use_tz": False,
        # set session time_zone
        "timezone": "Asia/Shanghai",
    }
