# -*- coding:utf-8 -*-  
# 
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include

from util.error import handle_400
from util.error import handle_403
from util.error import handle_404
from util.error import handle_500

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', include('main.urls', namespace='main', app_name = 'main')),
    url(r'^bbs/', include('bbs.urls', namespace='bbs', app_name='bbs')),
    url(r'^shop/', include('shop.urls', namespace='shop', app_name='shop')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += [
    url(r'^400.html$', handle_400),
    url(r'^403.html$', handle_403),
    url(r'^404.html$', handle_404),
    url(r'^500.html$', handle_500),
]

    

