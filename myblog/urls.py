#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: ziyi
# @Date  : 2018/11/9
# @Desc  :


from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_ziyi, name='index'),
    path('article/<int:article_id>', views.article_detail, name="article_detail"),
    path('article/', views.article_list, name="article_list"),
    path('type/<int:blog_type_pk>', views.article_with_type, name="article_with_type"),
]
