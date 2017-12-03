# -*- coding:utf-8 -*-  
#

from django.shortcuts import render
from api.generics import *
from main.models import *
from api.serializers import *
class CategoryView(ListCreateAPIView):
    model = CategoryModel
    serializer_class = CategorySerializer
    capabilities_prefetch = ['admin', 'update']


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    model = CategoryModel
    serializer_class = CategorySerializer
    

class UserView(ListCreateAPIView):
    model = User
    serializer_class = UserSerializer
    #capabilities_prefetch = ['admin', 'update']
    #

class UserDetail(RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer

   

