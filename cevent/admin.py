#encoding=utf-8

from django.contrib import admin
from cevent.models import Event, EventCat, EventBack, EventComment


@admin.register(EventCat)
class EventCatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'title')


@admin.register(EventBack)
class EventBackAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'content')


@admin.register(EventComment)
class EventCommentBackAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'content')


