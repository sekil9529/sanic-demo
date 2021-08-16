# coding: utf-8

import os
from typing import Dict, Any

from libs.config import Config

# 项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 日志文件路径
LOG_PATH = os.path.join(BASE_DIR, 'logs')

# 配置信息
CONFIG_INFO = Config(os.path.join(BASE_DIR, '.env')).format()


class BaseSettings:
    """配置基类"""

    DEBUG: bool = True

    # 随机秘钥
    SECRET_KEY: str

    # 关闭可提高性能
    ACCESS_LOG: bool = True

    # 跨域相关
    ENABLE_CORS: bool = False
    CORS_SUPPORTS_CREDENTIALS: bool = False

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URL: str
    # SQLAlchemy其他参数
    SQLALCHEMY_ENGINE_OPTIONS: Dict[str, Any] = {}

    # 日志配置
    BASE_LOGGING: Dict[str, Any] = {
        'version': 1,
        'loggers': {
            '': {
                'level': 'INFO',
                'handlers': ['console', 'info_file', 'error_file'],
                'propagate': False
            },
            'sanic': {
                'level': 'INFO',
                'handlers': ['console', 'info_file', 'error_file'],
                'propagate': False
            },
        },
        'formatters': {
            'default': {
                'format': '[%(asctime)s.%(msecs).3d] - [%(levelname)s] - [%(name)s:%(lineno)d] - [%(message)s]',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'default',
            },
            'info_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'info.log'),
                'maxBytes': 5 * 1024 * 1024,
                'backupCount': 10,
                'encoding': 'utf8',
                'level': 'INFO',
                'formatter': 'default',
            },
            'error_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'error.log'),
                'maxBytes': 5 * 1024 * 1024,
                'backupCount': 10,
                'encoding': 'utf8',
                'level': 'ERROR',
                'formatter': 'default',
            },
        },
    }
