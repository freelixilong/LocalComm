from django.contrib import admin# -*- coding:utf-8 -*-  
#
from django.conf.urls import url, include
from main.views import *

urlpatterns = [
    url(r'^category/$', CategoryView.as_view()), #获取所有一级分类,创建某个一级分类
    url(r'^category/(?P<pk>[0-9]+)/$', CategoryDetail.as_view()), #获取所有一级分类,创建某个一级分类
    url(r'^user/$', UserView.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$',UserDetail.as_view()),

]
