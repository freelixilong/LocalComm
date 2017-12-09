# -*- coding:utf-8 -*-  
#
from django.shortcuts import render
from api.generics import *
from bbs.models import *
from api.serializers import *
from django.db.models import F

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

class BBSUserSubArticles(SubListAPIView):
    model = Article
    serializer_class = BBSArticleSerializer
    parent_model = User
    relationship = 'articles'

class BBSUserCreateArticles(SubListCreateAPIView):
    model = Article
    serializer_class = BBSArticleSerializer
    parent_model = User
    relationship = 'articles'
    #parent_key = 'source_project_update'
    #new_in_320 = True  

class BBSGetArticleSubRes(SubListCreateAPIView):
    model = ResponseModel
    serializer_class = BBSResponseSerializer
    parent_model = Article
    relationship = 'articles' 

    def create(self, request, *args, **kwargs):
        parent = self.get_parent_object()
        if parent:
            parent.update_fields(res_num=F('res_num') + 1)

        return super(BBSGetArticleSubRes,self).create(request, *args, **kwargs)

class BBSResCreateRes(SubListCreateAPIView): #删除、获取某条回复，对某条回复进行回复
    model = ResponseModel
    serializer_class = BBSResCreateResSerializer
    parent_model = ResponseModel
    relationship = 'response_list'

class BBSResGetDelUp(RetrieveUpdateDestroyAPIView):
    model = ResponseModel
    serializer_class = BBSResCreateResSerializer

class BBSResSubRes(SubListAPIView):

    model = ResponseModel
    serializer_class = BBSResCreateResSerializer
    parent_model = ResponseModel
    relationship = 'response_list'

class BBSUserAllRes(SubListAPIView):
    model = ResponseModel
    serializer_class = BBSResCreateResSerializer
    parent_model = User
    relationship = 'response'
          




