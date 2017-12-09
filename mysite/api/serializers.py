
import copy
import json
import logging
import re
import six
import urllib
from collections import OrderedDict
#from dateutil import rrule

# Django
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist, ValidationError as DjangoValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text
from django.utils.text import capfirst
from django.utils.timezone import now
from django.utils.functional import cached_property

# Django REST Framework
from rest_framework.exceptions import ValidationError, PermissionDenied, ParseError
from rest_framework import fields
from rest_framework import serializers
from rest_framework import validators
from rest_framework.utils.serializer_helpers import ReturnList

from main.models import *
from bbs.models import *
#class BaseSerializer(serializers.ModelSerializer):
#
#    class Meta:
#        model = Snippet
#        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = ('name', 'logo', 'status')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'logo', 'passwd','sex','birth','wx_id','phone',
            'identity','nick','address','folder','email','sign','status','is_super')

class BBSCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BBSCategory
        fields = '__all__'

class BBSArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class BBSResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseModel
        fields = '__all__'

class BBSResCreateResSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseModel
        fields = '__all__'


