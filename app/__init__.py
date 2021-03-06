# coding: utf-8

from __future__ import annotations

from typing import Optional

from sanic import Sanic
from tortoise.contrib.sanic import register_tortoise

from app.blue import BLUE_TUPLE
from core.listeners import LISTENER_TUPLE, BaseListener
from core.middlewares import MIDDLEWARE_TUPLE, BaseMiddleware
from core.exception_handlers import EXC_HDL_TUPLE, BaseExcHandler
from settings import get_settings, BaseSettings


def create_app(env: Optional[str] = None) -> Sanic:
    """创建app"""

    # 获取配置
    settings: type[BaseSettings] = get_settings(env)

    # app创建
    app: Sanic = Sanic(__name__, log_config=getattr(settings, "BASE_LOGGING"))

    # sanic应用配置
    app.config.update_config(settings)

    # 注册监听
    register_listener(app, settings)

    # 注册tortoise
    register_tortoise(app, config=getattr(settings, "TORTOISE"), generate_schemas=False)

    # 注册中间件
    register_middleware(app)

    # 注册异常处理
    register_exception_handler(app)

    # 注册蓝图
    register_blueprint(app)

    return app


def register_blueprint(app: Sanic, prefix: Optional[str] = 'api') -> None:
    """注册蓝图"""
    for blueprint in BLUE_TUPLE:
        blueprint.url_prefix = '/'.join(url for url in (prefix, blueprint.url_prefix) if url)
        app.blueprint(blueprint)
    return None


def register_listener(app: Sanic, settings: type[BaseSettings]) -> None:
    """注册监听"""
    for listener_cls in LISTENER_TUPLE:
        listener: BaseListener = listener_cls(settings)
        for event in ('before_server_start', 'after_server_start', 'before_server_stop', 'after_server_stop'):
            if hasattr(listener, event):
                app.register_listener(getattr(listener, event), event)
    return None


def register_middleware(app: Sanic) -> None:
    """注册中间件"""
    for middle_cls in MIDDLEWARE_TUPLE:
        middle: BaseMiddleware = middle_cls()
        if hasattr(middle, 'before_request'):
            app.register_middleware(middle.before_request, attach_to='request')
        if hasattr(middle, 'before_response'):
            app.register_middleware(middle.before_response, attach_to='response')
    return None


def register_exception_handler(app: Sanic) -> None:
    """注册异常处理"""
    for exc_hdl_cls in EXC_HDL_TUPLE:
        exc_hdl: BaseExcHandler = exc_hdl_cls()
        app.error_handler.add(exc_hdl.get_exception(), exc_hdl.handle)
    return None
