#encoding=utf-8

from django.shortcuts import render
from blogs.models import Tag, Category, BaseModel
from common.helpers import paged_items, ok_json
from common.pc_m import judge_pc_or_mobile
from blogs.models import Category, Article


def blogs(request):
    nav_bar = "blog"
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    cat_id = int(request.GET.get("cat_id", 0))
    blog_cat_list = Category.objects.all()
    blog_list = Article.objects.filter(is_active=True).order_by("-id")
    if cat_id not in ["0", 0, ""]:
        blog_list = blog_list.filter(category__id=cat_id)
    if user_agt is False:
        blog_list = paged_items(request, blog_list)
        return render(request, 'web/pages/blog/blog.html', locals())
    else:
        blog_list = paged_items(request, blog_list)
        return render(request, 'web/pages/blog/blog.html', locals())


def blog_detail(request, id):
    nav_bar = "blog"
    blog_dtl = Article.objects.filter(id=id).first()
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if user_agt is False:
        return render(request, 'web/pages/blog/blog_detail.html', locals())
    else:
        return render(request, 'web/pages/blog/blog_detail.html', locals())