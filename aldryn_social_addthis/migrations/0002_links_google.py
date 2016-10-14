# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_social_addthis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='google',
            field=models.URLField(null=True, verbose_name='google', blank=True),
        ),
    ]
