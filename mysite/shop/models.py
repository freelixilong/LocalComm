# -*- coding:utf-8 -*-  
# 
from django.db import models
from django.utils.translation import ugettext_lazy as _
from main.models import BaseModel
from main.models import User
STATUS_CHOICES = [
    ('active', _('In Using')),
    ('delete', _('Deleted')),
    ('lock', _('Only view, cannot edit it')),
]
SHOP_CHOICES = [
    ('common', _('Common shop')),
    ('star', _('Star shop')),
]
COMMODITY_CHOICES = [
    ('off', _('Off the shelf')), #下架
    ('on', _('In the sale of')), # 在售
    ('empty', _('Commodity is empty')), #库存不足
]
SCORE_CHOICES = [
    (0, _('lowest')), 
    (1, _('score 1')), 
    (2, _('score 2')), 
    (3, _('score 3')),
    (4, _('score 4')), 
    (5, _('higest')), 
]
PRIVILEDGE_CHOICE = [
    ('owner', _('owner')),
    ('admin', _('shop adminitrator')),
    ('user', _('common user')),
]
ORDER_STATUS = [ #订单状态
    ('start', _('')),
    ('payed', _('')), #在线支付时会有这种状态
    ('sending', _('')),#正在派货
    ('cancel', _('canceled')),#取消
    ('received', _('received')),#已经接受，由消费者修改
    ('finish', _('finished')), #
]
PAY_CHOICES = [ #订单状态
    ('offline', _('')),
    ('online', _('pay on the line')), #在线支付时会有这种状态
]
class ShopCategory(BaseModel):
    name = models.CharField(max_length=128,)
    parent_id = models.ForeignKey(
        'ShopCategory',
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
        db_table = 'comm_category' #商品分类
        ordering = ('id',)

class Commodity(BaseModel):
    class Meta:
        #app_label = 'bbs'
        db_table = 'commodity' #商品分类
        ordering = ('id',)

    title = models.CharField(max_length=128,)
    sub_title = models.CharField(max_length=128,)
    images = models.CharField(max_length=128,)#相关图片存放路径
    price = models.DecimalField(max_digits=12, decimal_places=2,) #原价
    category = models.ForeignKey(
        'ShopCategory',
        related_name='commodities',
        blank=True,
        null=True,
        default=None,
        on_delete=models.SET_NULL,
    )
    owner = models.ForeignKey(
        'Shop',
        related_name='commodities',
        blank=False,
        default=None,
        on_delete=models.CASCADE,
    )
    discount_price = models.DecimalField(max_digits=12,decimal_places=2) #打折之后的价格
    second_hand = models.BooleanField(default=False,
        editable=True) #是不是二手商品
    sales = models.BooleanField(default=False,
        editable=True)  #是不是参加促销活动
    support_send = models.BooleanField(default=False,
        editable=True) #支持送货上门
    status = models.CharField(
        max_length=8,
        choices=COMMODITY_CHOICES,
        blank=False,
        default='on',
        verbose_name=_('On sale'),
        help_text=_(""),
    )

    detail = models.CharField(max_length=4096,)
    parameter = models.CharField(max_length=4096,)
    trans_condition = models.CharField(max_length=256,) #支持送货上门的条件，例如：3公里以内
    send_price = models.DecimalField(max_digits=12,decimal_places=2)#原价
    trans_price = models.DecimalField(max_digits=12,decimal_places=2)#原价
    #如果收货人在商家送货上门范围内，使用trans_price
    #send_price: 如果收货人不在发送范围内，为send_price

class CommResponse(BaseModel): #该表独立出来便宜快速查找
    class Meta:
        #app_label = 'bbs'
        db_table = 'comm_response' #商品分类
        ordering = ('id',)
    #
    #是否匿名发表 
    #anonymous           服务好-质量好-

    comm_id = models.ForeignKey(  #商品 ID
        'Commodity',
        related_name='comments',
        blank=False,
        on_delete=models.CASCADE,
    )
    parent_id = models.ForeignKey(
        'CommResponse',
        related_name='response_list',
        blank=False,
        on_delete=models.CASCADE,
    )
    content = models.CharField(max_length=1024,)
    author = models.ForeignKey(
        User,
        related_name='comm_response',
        blank=False,
        on_delete=models.CASCADE,
    )
    image = models.CharField(max_length=128,)
    #Image   score 
    score = models.IntegerField(
        blank=False,
        default=5,
        choices=SCORE_CHOICES,
        help_text=_(""),
    ) 
    anonymous = models.BooleanField(default=False,
        editable=True)

   
    
class Shop(BaseModel):
    name = models.CharField(max_length=128,)
    logo = models.CharField(max_length=128,)#相关图片存放路径
    serial_number = models.CharField(max_length=128,) #工商登记号
    phone = models.CharField(max_length=16)
    charge_indentity = models.CharField(max_length=18) #法人证件号,多指身份证号
    address = models.CharField(max_length=128,)
    shop_type = models.CharField(
        max_length=8,
        choices=SHOP_CHOICES,
        blank=False,
        default='common',
        verbose_name=_('common shop or start shop'),
        help_text=_(""),
    )
    category = models.ForeignKey(
        'ShopCategory',
        related_name='sub_shop',
        blank=True,
        null=True,
        default=None,
        on_delete=models.CASCADE,
    )
    zip_code = models.CharField(max_length=6,)

    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        blank=False,
        default='active',
        verbose_name=_('Current Status'),
        help_text=_(""),
    )
    pos = models.CharField(max_length=128,)  #gps 位置信息，暂时无用
   
    level = models.IntegerField(
        blank=False,
        default=0,
        help_text=_(""),
    )

    owner_id = models.ForeignKey(
        User,
        related_name='shops',
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
        db_table = 'shop'
        ordering = ('id',)

class UserShopLevel(BaseModel):
    class Meta:
        #app_label = 'bbs'
        db_table = 'shop_user_level'
        ordering = ('id',)
    user_id = models.ForeignKey(  #
        User,
        related_name='shop_level',
        blank=False,
        on_delete=models.CASCADE,
    )
    shop_id = models.ForeignKey(  #原始文章ID
        'Shop',
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
    )
    locked = models.BooleanField(default=False,
        editable=True)#禁止用户购买该商户的商品

class Ordered(BaseModel):
    class Meta:
        #app_label = 'bbs'
        db_table = 'ordered'
        ordering = ('id',)
    shop_id = models.ForeignKey(
        Shop,
        related_name='orders',
        blank=False,
        default=None,
        on_delete=models.CASCADE,
    )
    comm_id = models.ForeignKey(
        'Commodity',
        related_name='orders',
        blank=False,
        default=None,
        on_delete=models.CASCADE,
    )
  
    status = models.CharField(
        max_length=8,
        choices=ORDER_STATUS,
        blank=False,
        default='start',
    )
    pay_way = models.CharField(
        max_length=8,
        choices=PAY_CHOICES,
        blank=False,
        default='offline',
        
    )   
    commented = models.BooleanField(default=False,editable=True)#是否已经评论完毕  
    user_id = models.ForeignKey(User, related_name='orders',
        blank=False, on_delete=models.CASCADE,)
    contract_number = models.CharField(max_length=32)

    phone = models.CharField(max_length=16)  
    address = models.CharField(max_length=128)  
    title  = models.CharField(max_length=128)   
    sub_title = models.CharField(max_length=128)  
    pay_date = models.DateTimeField(auto_now_add=True) #这个时间不可靠  
    send_date = models.DateTimeField(null=True,default=None,) #这个时间不可靠 
    end_date = models.DateTimeField(auto_now =True)  
    number = models.IntegerField(blank=False,default=1)

    origin_price=models.DecimalField(max_digits=12,decimal_places=2)   
    sale_off_price = models.DecimalField(max_digits=12,decimal_places=2) #折后价
    trans_fee = models.DecimalField(max_digits=12,decimal_places=2) #运费


