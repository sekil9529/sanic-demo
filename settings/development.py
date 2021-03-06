# coding: utf-8

from __future__ import annotations

from .base import BaseSettings, CONFIG_INFO


class Settings(BaseSettings):
    """配置类"""

    SECRET_KEY: str = "*5}nAn#4GyQVO'*qq_2AAOC\\fXsvi9;m0.-Q|#jAcS"

    # 跨域相关
    ENABLE_CORS: bool = False
    CORS_SUPPORTS_CREDENTIALS: bool = False

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
                    "maxsize": 5,
                    # 注意：启动时直接创建5个session
                    "minsize": 5,
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

    REDIS: str = f"redis://" \
                 f":{CONFIG_INFO['redis']['password']}" \
                 f"@{CONFIG_INFO['redis']['host']}" \
                 f":{CONFIG_INFO['redis']['port']}" \
                 f"/{CONFIG_INFO['redis']['database']}" \
                 f"?max_connections=10"
