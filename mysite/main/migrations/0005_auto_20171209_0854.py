# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20171203_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='status',
            field=models.CharField(choices=[('active', 'In Using'), ('delete', 'Deleted'), ('lock', 'Only view, cannot edit it')], default='active', help_text='', max_length=16, verbose_name='Current Status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('M', 'male'), ('F', 'Female')], default='m', help_text='', max_length=1, verbose_name='male or female'),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('active', 'In Using'), ('delete', 'Deleted'), ('lock', 'Only view, cannot edit it')], default='active', help_text='', max_length=8, null=True, verbose_name='Current Status'),
        ),
    ]
