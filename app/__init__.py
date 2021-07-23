# coding: utf-8

import logging.config
from typing import Optional, Type

from sanic import Sanic

from app.blue import BLUE_TUPLE
from core.listeners import LISTENER_TUPLE
from settings import get_settings, BaseSettings


def create_app(env: Optional[str] = None) -> Sanic:
    """创建app"""

    app = Sanic(__name__)

    # 获取配置
    settings = get_settings(env)

    # 配置日志
    logging.config.dictConfig(settings.BASE_LOGGING)

    # sanic应用配置
    app.config.update_config(settings)

    # 注册监听
    register_listener(app, settings)

    # 注册蓝图
    register_blueprint(app)

    return app


def register_blueprint(app: Sanic) -> None:
    """注册蓝图"""
    for bp in BLUE_TUPLE:
        app.blueprint(bp)
    return None


def register_listener(app: Sanic, settings: Type[BaseSettings]) -> None:
    """注册监听"""
    for listener_cls in LISTENER_TUPLE:
        listener = listener_cls(settings)
        for event in ('before_server_start', 'after_server_start', 'before_server_stop', 'after_server_stop'):
            if hasattr(listener, event):
                app.register_listener(getattr(listener, event), event)
    return None
