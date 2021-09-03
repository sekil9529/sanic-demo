# coding: utf-8

from __future__ import annotations
import time
from typing import Any

from sanic import Request, json, HTTPResponse
from sqlalchemy.engine.row import Row
from sqlalchemy.engine.result import ChunkedIteratorResult
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import desc
from sqlalchemy.sql.selectable import Select

from app.models import User
from libs.logger import LoggerProxy
from libs.sqlalchemy.result import result_format

logger: LoggerProxy = LoggerProxy(__name__)


async def user_list(request: Request) -> HTTPResponse:
    """用户列表"""
    page: int = 1
    per_page: int = 5
    db_session: AsyncSession = request.ctx.db_session
    query: Select = select(User.id, User.name).select_from(User).order_by(desc(User.ctime), desc(User.id)). \
        offset((page - 1) * per_page).limit(per_page)
    async with db_session.begin():
        cur_result: ChunkedIteratorResult = await db_session.execute(query)
    result: list[Row] = cur_result.fetchall()
    data: list[dict[str, Any]] = result_format(result)
    # 测试慢日志中间件
    # time.sleep(1)
    return json({'data': data})
