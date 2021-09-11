#encoding=utf-8

from django.shortcuts import render
from blogs.models import Tag, Category, BaseModel
from common.helpers import paged_items, ok_json
from common.pc_m import judge_pc_or_mobile


def recovery_scheme(request):
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if user_agt is False:
        return render(request, 'web/pages/blog.html', locals())
    else:
        return render(request, 'web/pages/blog.html', locals())