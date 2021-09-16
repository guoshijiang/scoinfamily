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
from cevent.models import Event
from scauth.forms.update_pwd_form import UpdatePasswordForm
from scauth.forms.update_uinfo_form import UpdateUifForm


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
    login_way = request.GET.get("login_way", "password")
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if request.session.get("is_login", None):
        if user_agt is False:
            return redirect("index")
        else:
            return redirect("index")
    if request.method == "GET":
        if login_way == "password":
            login_form = UserPwdLoginForm(request)
        if login_way == "verify":
            login_form = UserCodeLoginForm(request)
        if user_agt is False:
            return render(request, 'web/pages/auth/login.html', locals())
        else:
            return render(request, 'web/pages/auth/login.html', locals())
    if request.method == "POST":
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
                    {
                        'login_form': login_form,
                        'error': error,
                        'login_way': "password"
                    }
                )
        if login_way == "verify":
            login_form = UserCodeLoginForm(request, request.POST)
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
                    {
                        'login_form': login_form,
                        'error': error,
                        'login_way': "verify",
                    }
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


def my_event(request):
    side_bar = 'my_event'
    user_id = request.session.get("user_id")
    user = AuthUser.objects.filter(id=user_id).first()
    event_list = Event.objects.filter(user=user).order_by("-id")
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if user_agt is False:
        return render(request, 'web/pages/auth/my_event.html', locals())
    else:
        return render(request, 'web/pages/auth/my_event.html', locals())


def update_password(request):
    side_bar = 'update_password'
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    user_id = request.session.get("user_id")
    user = AuthUser.objects.filter(id=user_id).first()
    if request.method == "GET":
        update_pwd_form = UpdatePasswordForm(user, request)
        if user_agt is False:
            return render(request, 'web/pages/auth/update_password.html', locals())
        else:
            return render(request, 'web/pages/auth/update_password.html', locals())
    if request.method == "POST":
        update_pwd_form = UpdatePasswordForm(user, request, request.POST)
        if update_pwd_form.is_valid():
            update_pwd_form.update_password()
            request.session["is_login"] = False
            return redirect("login")
        else:
            error = update_pwd_form.errors
            return render(
                request,
                "web/pages/auth/update_password.html",
                {'update_pwd_form': update_pwd_form, 'error': error}
            )


def update_uinfo(request):
    side_bar = 'update_uinfo'
    user_id = request.session.get("user_id")
    user = AuthUser.objects.filter(id=user_id).first()
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if request.method == "GET":
        uinfo_form = UpdateUifForm(request, user, instance=user)
        if user_agt is False:
            return render(request, 'web/pages/auth/update_uinfo.html', locals())
        else:
            return render(request, 'web/pages/auth/update_uinfo.html', locals())
    elif request.method == "POST":
        uinfo_form = UpdateUifForm(request, user, request.POST, request.FILES)
        if uinfo_form.is_valid():
            uinfo_form.save_user_info()
            return redirect("update_uinfo")
        else:
            error = uinfo_form.errors
            return render(
                request, "web/pages/auth/update_uinfo.html",
                {
                    'user': user,
                    'uinfo_form': uinfo_form,
                    'error': error
                }
            )
