# encoding=utf-8

import re
from django import forms
from scauth.models import AuthUser


class AuthUserRegisterForm(forms.Form):
    phone = forms.CharField(
        required=True,
        label="手机号",
        max_length=64,
        widget=forms.widgets.TextInput(
            {"placeholder": "手机号", "class": "el-input__inner"}
        ),
        error_messages={"required": "请输入手机号码, 手机号码不能为空"},
    )
    password = forms.CharField(
        required=True,
        label="密码",
        max_length=64,
        widget=forms.widgets.TextInput(
            {"type": "password", "placeholder": "请输入密码, 数字字母均可以长度大于8位小于20位", "class": "el-input__inner"}
        ),
        error_messages={"required": "请输入密码, 密码不能为空"},
    )
    c_password = forms.CharField(
        required=True,
        label="密码",
        max_length=64,
        widget=forms.widgets.TextInput(
            {"type": "password", "placeholder": "请输入确认密码", "class": "el-input__inner"}
        ),
        error_messages={"required": "请输入确认密码, 确认密码不能为空"},
    )
    # v_code = forms.CharField(
    #     required=True,
    #     label="验证码",
    #     max_length=64,
    #     widget=forms.widgets.TextInput(
    #         {"type": "password", "placeholder": "请输入验证码", "class": "el-input__inner"}
    #     ),
    #     error_messages={"required": "请输入验证码， 验证码不能为空"},
    # )

    def __init__(self, request, *args, **kw):
        self.request = request
        super(AuthUserRegisterForm, self).__init__(*args, **kw)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone in ["", None]:
            raise forms.ValidationError('手机号码不能为空')
        user_exist = AuthUser.objects.filter(phone=phone).first()
        if user_exist is not None:
            raise forms.ValidationError('该手机号已被注册, 请直接去登陆')
        return phone

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password in ["", None]:
            raise forms.ValidationError('密码不能为空')
        if not re.match('''[-`=\\\[\];',./~!@#$%^&*()_+|{}:"<>?A-Za-z0-9]{8,}$''', password):
            raise forms.ValidationError('密码设置不符合要求，需要大于8位, 可以是数字，字母和字符的组合')
        return password

    def clean_c_password(self):
        password = self.clean_password()
        c_password = self.cleaned_data.get('c_password')
        if c_password in ["", None]:
            raise forms.ValidationError('确认密码不能为空')
        if password != c_password:
            raise forms.ValidationError('两次输入的密码不一样')
        return c_password

    # def clean_v_code(self):
    #     v_code = self.cleaned_data.get('v_code')
    #     if v_code in ["", None]:
    #         raise forms.ValidationError('验证码不能为空')
    #     if v_code != "666666":
    #         raise forms.ValidationError('验证码不正确')
    #     return v_code

    def save_register_user(self):
        create_user = AuthUser.objects.create(
            phone=self.clean_phone(),
            password=self.clean_password(),
        )
        return create_user





