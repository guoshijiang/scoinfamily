# encoding=utf-8

from django.contrib import admin
from message.models import Message, MsgFriends


@admin.register(MsgFriends)
class MsgFriendsAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'is_active')


@admin.register(Message)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'msg_content', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'msg_content')

