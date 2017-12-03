# -*- coding:utf-8 -*-  
#
from django.shortcuts import render
from api.generics import *
from bbs.models import *
from api.serializers import *

class BBSCategoryView(ListCreateAPIView):
    model = BBSCategory
    serializer_class = BBSCategorySerializer

class BBSCategoryDetail(RetrieveUpdateDestroyAPIView):
    model = BBSCategory
    serializer_class = BBSCategorySerializer

class BBSCategorySub(SubListAPIView):

    model = BBSCategory
    serializer_class = BBSCategorySerializer
    parent_model = BBSCategory
    relationship = 'sub'

class BBSCategorySubArticles(SubListAPIView):
    model = Article
    serializer_class = BBSArticleSerializer
    parent_model = BBSCategory
    relationship = 'articles'

class BBSArticles(RetrieveUpdateDestroyAPIView):  #user article, cre
    model = Article
    serializer_class = BBSArticleSerializer

class BBSUserCreateArticles(SubListCreateAPIView):
    model = Article
    serializer_class = BBSArticleSerializer
    parent_model = User
    relationship = 'articles'
    #parent_key = 'source_project_update'
    #new_in_320 = True     



