# -*- coding:utf-8 -*-  
from django.db import models
from django.utils.timezone import now as tz_now
from django.utils.translation import ugettext_lazy as _
#User.add_to_class('get_queryset', get_user_queryset)
#User.add_to_class('can_access', check_user_access)
from bbs import SEX_CHOICE
from bbs import STATUS_CHOICES
class BaseModel(models.Model):
    '''
    Base model class with common methods for all models.
    '''
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

    def __unicode__(self):
        if hasattr(self, 'name'):
            return u'%s-%s' % (self.name, self.id)
        else:
            return u'%s-%s' % (self._meta.verbose_name, self.id)

    def clean_fields(self, exclude=None):
        '''
        Override default clean_fields to support methods for cleaning
        individual model fields.
        '''
        exclude = exclude or []
        errors = {}
        try:
            super(BaseModel, self).clean_fields(exclude)
        except ValidationError as e:
            errors = e.update_error_dict(errors)
        for f in self._meta.fields:
            if f.name in exclude:
                continue
            if hasattr(self, 'clean_%s' % f.name):
                try:
                    setattr(self, f.name, getattr(self, 'clean_%s' % f.name)())
                except ValidationError as e:
                    errors[f.name] = e.messages
        if errors:
            raise ValidationError(errors)

    def update_fields(self, **kwargs):
        save = kwargs.pop('save', True)
        update_fields = []
        for field, value in kwargs.items():
            if getattr(self, field) != value:
                setattr(self, field, value)
                update_fields.append(field)
        if save and update_fields:
            self.save(update_fields=update_fields)
        return update_fields

class CategoryModel(BaseModel):
    STATUS_CHOICES = [
        ('active', _('In Using')),
        ('delete', _('Deleted')),
        ('lock', _('Only view, cannot edit it')),
    ]

    name = models.CharField(max_length=128,)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    logo = models.CharField(max_length=128,)#logo存放路径
    status = models.CharField(
        max_length=16,
        choices=STATUS_CHOICES,
        blank=False,
        default='active',
        verbose_name=_('Current Status'),
        help_text=_(""),
    )
    class Meta:
        #app_label = 'main'
        db_table = 'category'
        ordering = ('id',)


class User(BaseModel):
    name = models.CharField(max_length=128,)
    logo = models.CharField(max_length=128,null= True)#logo存放路径
    passwd = models.CharField(max_length=256,null= True)
   
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICE,
        blank=False,
        default='m',
        verbose_name=_('male or female'),
        help_text=_(""),
    )
    birth = models.DateTimeField(null= True)
    wx_id = models.CharField(max_length=64,)
    phone = models.CharField(max_length=16,null= True)
    identity = models.CharField(max_length=18,null= True) #身份证号
    nick = models.CharField(max_length=64,null= True)
    address = models.CharField(max_length=128,null= True)
    folder = models.CharField(max_length=128,null= True) #个人上传的一些文件存放的路径
    email = models.EmailField(max_length=64,null= True)
    sign = models.CharField(max_length=64,null= True) #个人签名
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        blank=False,
        default='active',
        verbose_name=_('Current Status'),
        help_text=_(""),
        null= True
    )
    class Meta:
        #app_label = 'bbs'
        db_table = 'user'
        ordering = ('id',)
    def is_anonymous(self):
        if (self.name == "" or self.name == None) and\
           (self.wx_id == "" or self.wx_id == None):
           return True
        return False

    @property
    def is_superuser(self):
        return False
   
    




