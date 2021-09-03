# coding: utf-8

from __future__ import annotations

from sanic import Blueprint

from .demo.blue import bp as demo_bp
from .user.blue import bp as user_bp


BLUE_TUPLE: tuple[Blueprint, ...] = (
    demo_bp,
    user_bp,
)
