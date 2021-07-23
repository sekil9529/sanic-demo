# coding: utf-8

from datetime import datetime

from sqlalchemy import Column, BIGINT, VARCHAR, DATETIME
from sqlalchemy.dialects.mysql import TINYINT
from libs.sqlalchemy import Base


class User(Base):
    """用户表"""

    __tablename__ = 't_user'

    # 表的结构:
    id = Column(BIGINT, primary_key=True, autoincrement=True, comment='user表id')
    name = Column(VARCHAR(20), nullable=False, default='', comment='姓名')
    ctime = Column(DATETIME, nullable=False, default=datetime.now, comment='创建时间')
    utime = Column(DATETIME, nullable=False, onupdate=datetime.now, default=datetime.now, comment='更新时间')


class Follow(Base):
    """关注表"""

    __tablename__ = 't_follow'

    id = Column(BIGINT, primary_key=True, autoincrement=True, comment='follow表id')
    user_id = Column(BIGINT, nullable=False, comment='关注人id')
    usee_id = Column(BIGINT, nullable=False, comment='被关注人id')
    ctime = Column(DATETIME, nullable=False, default=datetime.now, comment='创建时间')
    utime = Column(DATETIME, nullable=False, onupdate=datetime.now, default=datetime.now, comment='更新时间')
    status = Column(TINYINT, nullable=False, default=1, comment='状态')
