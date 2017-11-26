from django.contrib import admin# -*- coding:utf-8 -*-  
#
from django.conf.urls import url, include
from main.views import CategoryView

urlpatterns = [
    url(r'^category/$', CategoryView.as_view()), #获取所有一级分类,创建某个一级分类
]