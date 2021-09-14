#encoding=utf-8

from django.shortcuts import redirect, render
from blogs.models import Tag, Category, BaseModel
from common.helpers import paged_items, ok_json
from common.pc_m import judge_pc_or_mobile
from cevent.models import Event, EventCat, EventBack, EventComment
from blogs.models import Article
from cevent.forms.pulish_form import EventForm
from scauth.models import AuthUser
from scauth.help import check_user_login


def event(request):
    nav_bar = "event"
    cat_id = int(request.GET.get("cat_id", 0))
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    blog_list = Article.objects.filter(is_active=True).order_by("-id")[0:6]
    event_feedback = EventBack.objects.filter(is_active=True).order_by("-id")[0:16]
    event_cat_list = EventCat.objects.all()
    event_list = Event.objects.filter(is_active=True).order_by("-id")
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
    cwindow = request.GET.get("cwindow", "")
    rwindow = request.GET.get("rwindow", "")
    pwindow = request.GET.get("pwindow", "")
    frpid = int(request.GET.get("frpid", 0))
    event = Event.objects.filter(id=vid).first()
    event_fb = EventBack.objects.filter(event=event).order_by("-id").first()
    event_comment_list = EventComment.objects.filter(event=event).order_by("-id")
    for event_comment in event_comment_list:
        event_comment.reply = event_comment_list.filter(father_event_cy=event_comment).order_by("-id")
        event_comment.reply_lastest = event_comment_list.filter(father_event_cy=event_comment).order_by("-id").first()
        event_comment.nums = event_comment_list.filter(father_event_cy=event_comment).count()
    event.views += 1
    event.save()
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if user_agt is False:
        event_comment_list = paged_items(request, event_comment_list)
        return render(request, 'web/pages/event/event_detail.html', locals())
    else:
        event_comment_list = paged_items(request, event_comment_list)
        return render(request, 'web/pages/event/event_detail.html', locals())


@check_user_login
def publish_event(request):
    nav_bar = "event"
    user_id = request.session.get("user_id")
    user = AuthUser.objects.filter(id=user_id).first()
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if request.method == "GET":
        event_form = EventForm(request)
        if user_agt is False:
            return render(request, 'web/pages/event/publish_event.html', locals())
        else:
            return render(request, 'web/pages/event/publish_event.html', locals())
    if request.method == "POST":
        event_form = EventForm(request, request.POST)
        if event_form.is_valid():
            Event.objects.create(
                user=user,
                event_cat=event_form.clean_event_cat(),
                email=event_form.clean_email(),
                weichat=event_form.clean_weichat(),
                coin=event_form.clean_coin(),
                my_address=event_form.clean_my_address(),
                hacker_address=event_form.clean_hacker_address(),
                title=event_form.clean_title(),
                detail=event_form.clean_detail(),
                is_public=event_form.clean_is_public(),
            )
            return redirect("event")


@check_user_login
def event_cmt_reply(request, eid):
    father_event_id = int(request.POST.get("father_event_id", 0))
    content = request.POST.get("content", "")
    user_id = int(request.session.get("user_id"))
    user = AuthUser.objects.filter(id=user_id).first()
    event = Event.objects.filter(id=eid).order_by("-id").first()
    if father_event_id not in ["0", 0]:
        father_event_cy=EventComment.objects.filter(id=father_event_id).first()
    else:
        father_event_cy = None
    EventComment.objects.create(
        user=user,
        event=event,
        father_event_cy=father_event_cy,
        content=content,
    )
    return redirect("event_detail", eid)


