#encoding=utf-8

from typing import Any, List
from django.urls import path, re_path, include
from common.views import index
from cevent.views import (
    event,
    event_detail,
    publish_event
)
from blogs.views import (
    blogs,
    blog_detail
)
from tools.views import (
    tools,
    tools_detail
)
from scauth.views import (
    sms_send,
    login,
    register,
    forget,
    logout,
    my_event,
    update_password,
    update_uinfo
)


urlpatterns: List[Any] = [
    path(r'', index, name='index'),
    path(r'event', event, name='event'),
    path(r'<int:vid>/event_detail', event_detail, name='event_detail'),
    path(r'publish_event', publish_event, name='publish_event'),

    path(r'blogs', blogs, name='blogs'),
    path(r'<int:id>/blog_detail', blog_detail, name='blog_detail'),

    path(r'tools', tools, name='tools'),
    path(r'<int:tid>/tools_detail', tools_detail, name='tools_detail'),

    path(r'sms_send', sms_send, name='sms_send'),
    path(r'logout', logout, name='logout'),
    path(r'login', login, name='login'),
    path(r'register', register, name='register'),
    path(r'forget', forget, name='forget'),
    path(r'my_event', my_event, name='my_event'),
    path(r'update_password', update_password, name='update_password'),
    path(r'update_uinfo', update_uinfo, name='update_uinfo'),
]