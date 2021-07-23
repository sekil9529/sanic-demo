# coding: utf-8

import logging.config
from typing import Optional, Type

from sanic import Sanic

from app.blue import BLUE_TUPLE
from core.listeners import LISTENER_TUPLE
from core.middlewares import MIDDLEWARE_TUPLE
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

    # 注册中间件
    register_middleware(app)

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


def register_middleware(app: Sanic) -> None:
    """注册中间件"""
    for middle_cls in MIDDLEWARE_TUPLE:
        middle = middle_cls(app)
        if hasattr(middle, 'before_request'):
            app.register_middleware(middle.before_request, attach_to='request')
        if hasattr(middle, 'before_response'):
            app.register_middleware(middle.before_response, attach_to='response')
    return None
