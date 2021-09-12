#encoding=utf-8

from django.shortcuts import render
from blogs.models import Tag, Category, BaseModel
from common.helpers import paged_items, ok_json
from common.pc_m import judge_pc_or_mobile
from cevent.models import Event, EventCat, EventBack
from blogs.models import Article


def event(request):
    nav_bar = "event"
    cat_id = int(request.GET.get("cat_id", 0))
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    blog_list = Article.objects.filter(is_active=True).order_by("-id")[0:6]
    event_feedback = EventBack.objects.filter(is_active=True).order_by("-id")[0:16]
    event_cat_list = EventCat.objects.all()
    event_list = Event.objects.filter(status__in=["WAIT_SOLUTE", "WAIT_BACK", "FINISH"]).order_by("-id")
    if cat_id not in [0, "0", None]:
        event_list = event_list.filter(event_cat__id=cat_id)
    if user_agt is False:
        event_list = paged_items(request,event_list)
        return render(request, 'web/pages/event/event.html', locals())
    else:
        event_list = paged_items(request, event_list)
        return render(request, 'web/pages/event/event.html', locals())


def event_detail(request, vid):
    nav_bar = "event"
    event = Event.objects.filter(id=vid).first()
    event_fb = EventBack.objects.filter(event=event).order_by("-id").first()
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if user_agt is False:
        return render(request, 'web/pages/event/event_detail.html', locals())
    else:
        return render(request, 'web/pages/event/event_detail.html', locals())


def publish_event(request):
    nav_bar = "event"
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if user_agt is False:
        return render(request, 'web/pages/event/publish_event.html', locals())
    else:
        return render(request, 'web/pages/event/publish_event.html', locals())
