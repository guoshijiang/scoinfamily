#encoding=utf-8

from django.shortcuts import render
from blogs.models import Tag, Category, BaseModel
from common.helpers import paged_items, ok_json
from common.pc_m import judge_pc_or_mobile
from tools.models import Tools


def tools(request):
    nav_bar = "tools"
    tools_list = Tools.objects.filter(is_active=True).order_by("-id")
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if user_agt is False:
        tools_list = paged_items(request, tools_list)
        return render(request, 'web/pages/tools/tools.html', locals())
    else:
        tools_list = paged_items(request, tools_list)
        return render(request, 'web/pages/tools/tools.html', locals())


def tools_detail(request, tid):
    nav_bar = "tools"
    tool_detail = Tools.objects.filter(id=tid).first()
    tool_detail.views += 1
    tool_detail.save()
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if user_agt is False:
        return render(request, 'web/pages/tools/tools_detail.html', locals())
    else:
        return render(request, 'web/pages/tools/tools_detail.html', locals())