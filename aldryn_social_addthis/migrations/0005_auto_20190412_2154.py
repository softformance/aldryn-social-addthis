# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-12 19:54


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_social_addthis', '0004_auto_20161014_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='google',
        ),
        migrations.RemoveField(
            model_name='links',
            name='google',
        ),
    ]
