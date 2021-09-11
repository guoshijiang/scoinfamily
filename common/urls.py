#encoding=utf-8

from typing import Any, List
from django.urls import path, re_path, include
from common.views import index
from cevent.views import event
from blogs.views import recovery_scheme
from tools.views import tools
from scauth.views import login, register


urlpatterns: List[Any] = [
    path(r'', index, name='index'),
    path(r'event', event, name='event'),
    path(r'recovery_scheme', recovery_scheme, name='recovery_scheme'),
    path(r'tools', tools, name='tools'),

    path(r'login', login, name='login'),
    path(r'register', register, name='register'),
]