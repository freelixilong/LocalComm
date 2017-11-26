# -*- coding:utf-8 -*-  
# 

# Python
import urllib
import logging

# Django
from django.conf import settings
from django.utils.timezone import now as tz_now
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _

# Django REST Framework
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework import HTTP_HEADER_ENCODING
from main.models import User
class LoggedBasicAuthentication(authentication.BasicAuthentication):
    models = User
    def authenticate(self, request):
       
        ret = super(LoggedBasicAuthentication, self).authenticate(request)
        if ret:
            username = ret[0].name if ret[0] else '<none>'
            #logger.debug(smart_text(u"User {} performed a {} to {} through the API".format(username, request.method, request.path)))
        return ret

    def authenticate_credentials(self, userid, password, request=None):
        """
        Authenticate the userid and password against username and password
        with optional request for context.
        """
        #import pdb
        #pdb.set_trace()
        user = User.objects.filter(wx_id=userid)
        print(user)
        if user is None:
            raise exceptions.AuthenticationFailed(_('Invalid username'))

        return (user[0], None)
    def authenticate_header(self, request):
       
        user_id = request.META.get("USER")
        if not user_id:
            user_id = request.META.get("USER_NAME")
        return user_id
       
