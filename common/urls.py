#encoding=utf-8

from typing import Any, List
from django.urls import path, re_path, include
from common.views import index
from cevent.views import (
    event,
    event_detail,
    publish_event
)
from blogs.views import recovery_scheme
from tools.views import (
    tools,
    tools_detail
)
from scauth.views import login, register


urlpatterns: List[Any] = [
    path(r'', index, name='index'),
    path(r'event', event, name='event'),
    path(r'<int:vid>/event_detail', event_detail, name='event_detail'),
    path(r'publish_event', publish_event, name='publish_event'),

    path(r'recovery_scheme', recovery_scheme, name='recovery_scheme'),

    path(r'tools', tools, name='tools'),
    path(r'<int:tid>/tools_detail', tools_detail, name='tools_detail'),


    path(r'login', login, name='login'),
    path(r'register', register, name='register'),
]