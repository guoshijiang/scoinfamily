# encoding=utf-8

from django.contrib import admin
from tools.models import Tools


@admin.register(Tools)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')


