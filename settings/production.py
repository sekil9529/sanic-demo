# coding: utf-8

from typing import Dict, Any

from .base import BaseSettings, CONFIG_INFO


class Settings(BaseSettings):
    """配置类"""

    SECRET_KEY: str = 'wdATN(TPpSB-269m0Ayd9[H+^:/TZW;qkIJD8a:-K{'

    ACCESS_LOG: bool = False

    # 跨域相关
    ENABLE_CORS: bool = True
    CORS_SUPPORTS_CREDENTIALS: bool = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URL: str = f"mysql+aiomysql://{CONFIG_INFO['db']['user']}:{CONFIG_INFO['db']['password']}" \
                                   f"@{CONFIG_INFO['db']['host']}/{CONFIG_INFO['db']['database']}?charset=utf8mb4"
    SQLALCHEMY_ENGINE_OPTIONS: Dict[str, Any] = {
        'pool_size': 10,
        'max_overflow': 0,
        'pool_recycle': 60 * 60 * 2,
        # 'pool_reset_on_return': None,  # 放回时执行的操作，默认执行 'rollback'
        'pool_timeout': 5,  # n秒获取不到session, 超时报错
        'isolation_level': 'READ COMMITTED',
        'echo_pool': True,
        'pool_pre_ping': False,
        'execution_options': {
        }
    }
