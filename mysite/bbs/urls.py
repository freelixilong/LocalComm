# -*- coding:utf-8 -*-  
#
from django.conf.urls import url, include
#from bbs.views import BBSCategory

urlpatterns = [
    #url(r'^category/$', BBSCategory.as_view()), #获取所有一级分类,创建某个一级分类
    ##url(r'^category/(?P<pk>[0-9]+)/sub/$', bbs.views.get_category_subs), #获取某个分类所有的子分类，创建某个分类的子类
    #url(r'^category/(?P<pk>[0-9]+)/articles/$', bbs.views.get_category_articles), #获取某个分类所有的文章，创建某个分类的文章
    #url(r'^articles/(?P<pk>[0-9]+)/$',bbs.views.get_article_by_id ), #获取某个文章
    #url(r'^articles/(?P<pk>[0-9]+)/sub/$', bbs.views.get_response_by_article_id), #获取对某个文章的回复

    #url(r'^user/(?P<pk>[0-9]+)/articles/$', bbs.views.get_articles_by_user_id), #获取某个用户的所有文章
    #url(r'^user/(?P<pk>[0-9]+)/response/$', bbs.views.get_responses_by_user_id), #获取某个用户的所有回复

]