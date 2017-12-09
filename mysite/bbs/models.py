# -*- coding:utf-8 -*-  
# 
from django.db import models
#
from django.utils.translation import ugettext_lazy as _
from main.models import BaseModel
from main.models import User
# Create your models here.
STATUS_CHOICES = [
    ('active', _('In Using')),
    ('delete', _('Deleted')),
    ('lock', _('Only view, cannot edit it')),
]
SEX_CHOICE = [
    ('M', _('male')),
    ('F', _('Female')),
]
PRIVILEDGE_CHOICE = [
    ('super', _('super administrator')),
    ('admin', _('board adminitrator')),
    ('user', _('common user')),
]

class BBSCategory(BaseModel):
    name = models.CharField(max_length=128,)
    parent_id = models.ForeignKey(
        'BBSCategory',
        related_name='sub',
        blank=True,
        null=True,
        default=None,
        on_delete=models.CASCADE,
    )
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        blank=False,
        default='active',
        verbose_name=_('Current Status'),
        help_text=_(""),
    )
    class Meta:
        #app_label = 'bbs'
        db_table = 'bbs_category'
        ordering = ('id',)

class Article(BaseModel):
    title = models.CharField(max_length=128,)
    content = models.CharField(max_length=4096,)
    author = models.ForeignKey(
        User,
        related_name='articles',
        blank=False,
        on_delete=models.CASCADE,
    )
    images = models.CharField(max_length=128,)#相关图片存放路径
    category = models.ForeignKey(
        'BBSCategory',
        related_name='articles',
        blank=False,
        on_delete=models.CASCADE,
    )
    anonymous = models.BooleanField(default=False,
        editable=True)
    prohibit_res = models.BooleanField(default=False,
        editable=True)#禁止回复?
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        blank=False,
        default='active',
        verbose_name=_('Current Status'),
        help_text=_(""),
    )
    res_num = models.IntegerField(
        blank=False,
        default=0,
        help_text=_(""), #对本帖子的回复计数
    )
    class Meta:
        #app_label = 'bbs'
        db_table = 'bbs_article'
        ordering = ('id',) 

class ResponseModel(BaseModel): #该表独立出来便宜快速查找
    origin_id = models.ForeignKey(  #原始文章ID
        'Article',
        related_name='articles',
        blank=False,
        on_delete=models.CASCADE,
    )
    parent_id = models.ForeignKey(
        'ResponseModel',
        related_name='response_list',
        null=True,
        on_delete=models.CASCADE,
    )
    content = models.CharField(max_length=4096,)
    author = models.ForeignKey(
        User,
        related_name='response',
        blank=False,
        on_delete=models.CASCADE,
    )
    anonymous = models.BooleanField(default=False,
        editable=True)

    res_num = models.IntegerField(
        blank=False,
        default=0,
        help_text=_(""), #对本帖子的回复计数
    )
    is_new = models.BooleanField(default=True,
        editable=True)
    prohibit_res = models.BooleanField(default=False,
        editable=True)#禁止回复?
    class Meta:
        #app_label = 'bbs'
        db_table = 'bbs_response'
        ordering = ('id',) 

class UserBoardLevel(BaseModel):
    class Meta:
        #app_label = 'bbs'
        db_table = 'bbs_user_level'
        ordering = ('id',)
    user_id = models.ForeignKey(  #
        User,
        related_name='board_level',
        blank=False,
        on_delete=models.CASCADE,
    )
    board_id = models.ForeignKey(  #
        'BBSCategory',
        related_name='+',
        blank=False,
        on_delete=models.CASCADE,
    )
    level = models.IntegerField(
        blank=False,
        default=0,
        help_text=_(""),
    )
    privilege = models.CharField(
        max_length=8,
        choices=PRIVILEDGE_CHOICE,
        blank=False,
        default='user',
        #verbose_name=_(''),
        #help_text=_(""),
    )
    locked = models.BooleanField(default=False,
        editable=True)


            
                        
          



             



