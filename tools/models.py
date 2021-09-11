#encoding=utf-8


from django.db import models
from DjangoUeditor.models import UEditorField
from common.models import BaseModel


class Tools(BaseModel):
    name = models.CharField(
        max_length=70,
        default='',
        verbose_name='工具名称'
    )
    excerpt = models.TextField(
        max_length=200,
        default='',
        verbose_name='工具简介'
    )
    img = models.ImageField(
        upload_to='article/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name='工具封面'
    )
    github = models.CharField(
        max_length=70,
        default='',
        verbose_name='工具github地址'
    )
    body = UEditorField(
        width=800, height=500,
        toolbars="full", imagePath="upimg/", filePath="upfile/",
        upload_settings={"imageMaxSize": 1204000},
        settings={}, command=None, blank=True, verbose_name='工具详细介绍'
    )
    views = models.PositiveIntegerField(default=0, verbose_name='查看次数')
    is_active = models.BooleanField(default=True, verbose_name='是否有效')

    class Meta:
        verbose_name = '工具表'
        verbose_name_plural = '工具表'

    def __str__(self):
        return self.name

    def return_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
