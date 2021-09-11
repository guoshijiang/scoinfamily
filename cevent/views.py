#encoding=utf-8

from django.shortcuts import render
from blogs.models import Tag, Category, BaseModel
from common.helpers import paged_items, ok_json
from common.pc_m import judge_pc_or_mobile


def event(request):
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if user_agt is False:
        return render(request, 'web/pages/event/event.html', locals())
    else:
        return render(request, 'web/pages/event/event.html', locals())


def event_detail(request, vid):
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if user_agt is False:
        return render(request, 'web/pages/event/event_detail.html', locals())
    else:
        return render(request, 'web/pages/event/event_detail.html', locals())


def publish_event(request):
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if user_agt is False:
        return render(request, 'web/pages/event/publish_event.html', locals())
    else:
        return render(request, 'web/pages/event/publish_event.html', locals())
