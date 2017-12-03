# -*- coding:utf-8 -*-  
#
from django.conf.urls import url, include
#from bbs.views import BBSCategory
from bbs.views import *

urlpatterns = [
    url(r'^category/$', BBSCategoryView.as_view()), #获取所有一级分类,创建某个一级分类 create del update get.
    url(r'^category/(?P<pk>[0-9]+)/$', BBSCategoryDetail.as_view()), #获取所有一级分类,创建某个一级分类, only get
    url(r'^category/(?P<pk>[0-9]+)/sub/$', BBSCategorySub.as_view()), #获取某个分类所有的子分类,Only Get
    url(r'^category/(?P<pk>[0-9]+)/articles/$', BBSCategorySubArticles.as_view()), #获取某个分类所有的文章，get
    
    url(r'^articles/(?P<pk>[0-9]+)/$',BBSArticles.as_view()), #获取某个文章，修改，删除---|同以下API构成一个完整的操作
    url(r'^user/(?P<pk>[0-9]+)/articles/$', BBSUserCreateArticles.as_view()), #用户创建文章----|
    url(r'^articles/(?P<pk>[0-9]+)/sub/$', BBSGetArticleSubRes.as_view()), #获取对某个文章的回复
    url(r'^user/(?P<pk>[0-9]+)/subs/$', BBSUserSubArticles.as_view()), #获取某个用户的所有文章
    #url(r'^user/(?P<pk>[0-9]+)/response/$', bbs.views.get_responses_by_user_id), #获取某个用户的所有回复

]