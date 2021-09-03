# coding: utf-8

import time

from sanic import Request, json, HTTPResponse
from sqlalchemy.future import select
from sqlalchemy import desc
from app.models import User
from libs.logger import LoggerProxy
from libs.sqlalchemy.result import result_format

logger: LoggerProxy = LoggerProxy(__name__)


async def user_list(request: Request) -> HTTPResponse:
    """用户列表"""
    page = 1
    per_page = 5
    db_session = request.ctx.db_session
    query = select(User.id, User.name).select_from(User).order_by(desc(User.ctime), desc(User.id)). \
        offset((page - 1) * per_page).limit(per_page)
    async with db_session.begin():
        cur_result = await db_session.execute(query)
    result = cur_result.fetchall()
    data = result_format(result)
    # 测试慢日志中间件
    # time.sleep(1)
    return json({'data': data})
