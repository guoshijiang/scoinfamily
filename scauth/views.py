#encoding=utf-8

from django.shortcuts import redirect, render
from blogs.models import Tag, Category, BaseModel
from common.helpers import paged_items, ok_json
from common.pc_m import judge_pc_or_mobile
from scauth.help import get_code, send_msg_by_ali
from django.core.cache import cache
from scauth.forms.regist_form import AuthUserRegisterForm
from scauth.forms.login_form import UserPwdLoginForm, UserCodeLoginForm


def sms_send(request):
    phone = request.GET.get('phone')
    code = "666666"
    cache.set(phone, code, 60)
    if cache.has_key(phone):
        # result = send_msg_by_ali(phone, code)
        return ok_json("success")


def register(request):
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if request.method == "GET":
        register_form = AuthUserRegisterForm(request)
        if user_agt is False:
            return render(request, 'web/pages/auth/register.html', locals())
        else:
            return render(request, 'web/pages/auth/register.html', locals())
    if request.method == "POST":
        register_form = AuthUserRegisterForm(request, request.POST)
        if register_form.is_valid():
            register_form.save_register_user()
            return redirect("login")
        else:
            error = register_form.errors
            return render(
                request,
                'web/pages/auth/register.html',
                {'register_form': register_form, 'error': error}
            )


def login(request):
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if request.session.get("is_login", None):
        if user_agt is False:
            return redirect("index")
        else:
            return redirect("index")
    if request.method == "GET":
        login_way = request.GET.get("login_way", "password")
        if login_way == "password":
            login_form = UserPwdLoginForm(request)
        else:
            login_form = UserCodeLoginForm(request)
        if user_agt is False:
            return render(request, 'web/pages/auth/login.html', locals())
        else:
            return render(request, 'web/pages/auth/login.html', locals())
    if request.method == "POST":
        login_way = request.POST.get("login_way", "password")
        if login_way == "password":
            login_form = UserPwdLoginForm(request, request.POST)
            if login_form.is_valid():
                pass
        else:
            login_form = UserCodeLoginForm(request, request.POST)
            if login_form.is_valid():
                pass


def forget(request):
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if user_agt is False:
        return render(request, 'web/pages/auth/forget.html', locals())
    else:
        return render(request, 'web/pages/auth/forget.html', locals())
