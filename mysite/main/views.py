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

   

