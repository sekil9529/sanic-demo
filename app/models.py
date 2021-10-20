# coding: utf-8

from tortoise import fields
from tortoise.models import Model


class User(Model):
    """用户表"""

    class Meta:
        table = "t_user"
        table_description = "用户表"

    id = fields.BigIntField(pk=True, description="表id")
    name = fields.CharField(max_length=20, null=False, default="", description="姓名")
    ctime = fields.DatetimeField(null=False, auto_now_add=True, description="创建时间")
    utime = fields.DatetimeField(null=False, auto_now=True, description="更新时间")


class Follow(Model):
    """关注表"""

    class Meta:
        table = "t_follow"
        table_description = "关注表"

    id = fields.BigIntField(pk=True, description="表id")
    user = fields.ForeignKeyField("models.User", db_constraint=False, index=True, null=False,
                                  related_name="rel_follow_user", description="关注人id")
    usee = fields.ForeignKeyField("models.User", db_constraint=False, index=True, null=False,
                                  related_name="rel_follow_usee", description="被关注人id")
    status = fields.BooleanField(null=False, default=1, description="状态")
    ctime = fields.DatetimeField(null=False, auto_now_add=True, description="创建时间")
    utime = fields.DatetimeField(null=False, auto_now=True, description="更新时间")
