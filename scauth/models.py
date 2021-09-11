# encoding=utf-8

from django.db import models
from common.models import BaseModel


class AuthUser(BaseModel):
    name = models.CharField(
        max_length=100,
        default="coinfamily",
        verbose_name="用户名",
    )
    password = models.CharField(
        max_length=100,
        default="",
        verbose_name="用户密码",
    )
    photo = models.ImageField(
        upload_to="user_img/%Y/%m/%d/",
        verbose_name="头像",
        blank=True,
        null=True,
    )
    phone = models.CharField(
        max_length=100,
        default="",
        verbose_name="手机号码",
    )
    eamail = models.CharField(
        max_length=100,
        default="",
        verbose_name="邮箱",
    )
    weichat = models.CharField(
        max_length=100,
        default="",
        verbose_name="微信",
    )
    telegram = models.CharField(
        max_length=100,
        default="",
        verbose_name="电报账号",
    )
    login_count = models.PositiveIntegerField(
        default=0,
        verbose_name="登陆次数"
    )
    token = models.CharField(
        max_length=100,
        default="",
        blank=True,
        null=True,
        verbose_name="用户token",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="是否是有效"
    )

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = "用户表"

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }
