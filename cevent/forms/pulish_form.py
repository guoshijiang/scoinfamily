# encoding=utf-8

import re
from django import forms
from cevent.models import Event, EventCat
from DjangoUeditor.forms import UEditorField


class EventForm(forms.ModelForm):
    coin = forms.CharField(
        required=True,
        label="币种",
        max_length=64,
        widget=forms.widgets.TextInput(
            {"placeholder": "请输入币种", "id": "inputEmail3"}
        ),
        error_messages={"required": "请输入币种, 币种不能为空"},
    )
    my_address = forms.CharField(
        required=False,
        label="我的地址",
        max_length=64,
        widget=forms.widgets.TextInput(
            {"type": "password", "placeholder": "请输入自己的地址(选填)", "class": "el-input__inner"}
        )
    )
    hacker_address = forms.CharField(
        required=False,
        label="黑客地址",
        max_length=64,
        widget=forms.widgets.TextInput(
            {"type": "password", "placeholder": "请输入黑客地址(选填)", "class": "el-input__inner"}
        )
    )
    event_cat = forms.ModelChoiceField(
        empty_label="请选择",
        queryset=EventCat.objects.filter(is_active=True)
    )
    is_public = forms.CharField(
        label="是否公开",
        initial=2,
        widget=forms.Select(
            choices=(('Yes', '公开'), ('No', '不公开'),)
        ),
    )
    title = forms.CharField(
        required=True,
        label="标题",
        max_length=64,
        widget=forms.widgets.TextInput(
            {"type": "password", "placeholder": "请输入自己的地址(必填)", "class": "el-input__inner"}
        )
    )
    detail = UEditorField(
        label='文章内容',
        width=800,
        height=900,
        toolbars="full",
        imagePath="upimg/",
        filePath="upfile/",
        upload_settings={"imageMaxSize": 1204000},
        settings={}
    )
    email = forms.CharField(
        required=True,
        label="邮箱",
        max_length=64,
        widget=forms.widgets.TextInput(
            {"type": "password", "placeholder": "请输入自己的邮箱(必填)", "class": "el-input__inner"}
        )
    )
    weichat = forms.CharField(
        required=True,
        label="微信",
        max_length=64,
        widget=forms.widgets.TextInput(
            {"type": "password", "placeholder": "请输入自己的微信(必填)", "class": "el-input__inner"}
        )
    )

    class Meta:
        model = Event
        fields = [
            'coin', 'my_address', 'hacker_address', 'is_public', 'title', 'detail', 'email', 'weichat'
        ]

    def __init__(self, request, *args, **kw):
        self.request = request
        super(EventForm, self).__init__(*args, **kw)

    def clean_coin(self):
        coin = self.cleaned_data.get('coin')
        if coin in ["", None]:
            raise forms.ValidationError('币种不能为空')
        return coin

    def clean_my_address(self):
        my_address = self.cleaned_data.get('my_address')
        return my_address

    def clean_hacker_address(self):
        hacker_address = self.cleaned_data.get('hacker_address')
        return hacker_address

    def clean_is_public(self):
        is_public = self.cleaned_data.get('is_public')
        return is_public

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title in ["", None]:
            raise forms.ValidationError('标题不能为空')
        return title

    def clean_detail(self):
        detail = self.cleaned_data.get('detail')
        if detail in ["", None]:
            raise forms.ValidationError('内容不能为空')
        return detail

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email in ["", None]:
            raise forms.ValidationError('邮箱不能为空')
        return email

    def clean_weichat(self):
        weichat = self.cleaned_data.get('weichat')
        if weichat in ["", None]:
            raise forms.ValidationError('微信不能为空')
        return weichat
