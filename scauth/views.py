#encoding=utf-8

from django.shortcuts import redirect, render
from blogs.models import Tag, Category, BaseModel
from common.helpers import paged_items, ok_json
from common.pc_m import judge_pc_or_mobile
from scauth.help import get_code, send_msg_by_ali
from django.core.cache import cache
from scauth.forms.regist_form import AuthUserRegisterForm
from scauth.forms.login_form import UserPwdLoginForm, UserCodeLoginForm
from scauth.forms.forget_form import ForgetPasswordForm
from scauth.models import AuthUser


def sms_send(request):
    phone = request.GET.get('phone')
    code = "666666"
    cache.set(phone, code, 60)
    if cache.has_key(phone):
        # result = send_msg_by_ali(phone, code)
        return ok_json("success")


def logout(request):
    if not request.session.get("is_login", None):
        return redirect("index")
    request.session.flush()
    return redirect("index")


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
                user = AuthUser.objects.filter(phone=login_form.clean_phone()).first()
                request.session["is_login"] = True
                request.session["user_id"] = user.id
                request.session["user_name"] = user.name
                request.session["user_pho"] = user.photo
                return redirect("index")
            else:
                error = login_form.errors
                return render(
                    request,
                    'web/pages/auth/login.html',
                    {'login_form': login_form, 'error': error}
                )
        else:
            login_form = UserCodeLoginForm(request, request.POST)
            user = AuthUser.objects.filter(phone=login_form.clean_phone()).first()
            if login_form.is_valid():
                request.session["is_login"] = True
                request.session["user_id"] = user.id
                request.session["user_name"] = user.name
                request.session["user_pho"] = user.photo
                return redirect("index")
            else:
                error = login_form.errors
                return render(
                    request,
                    'web/pages/auth/login.html',
                    {'login_form': login_form, 'error': error}
                )


def forget(request):
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if request.method == "GET":
        forget_form = ForgetPasswordForm(request)
        if user_agt is False:
            return render(request, 'web/pages/auth/forget.html', locals())
        else:
            return render(request, 'web/pages/auth/forget.html', locals())
    if request.method == "POST":
        forget_form = ForgetPasswordForm(request, request.POST)
        if forget_form.is_valid():
            user = AuthUser.objects.filter(phone=forget_form.clean_phone()).first()
            forget_form.update_password(user)
            return redirect("login")
        else:
            error = forget_form.errors
            return render(
                request,
                "web/pages/auth/forget.html",
                { 'forget_form': forget_form, 'error': error}
            )



