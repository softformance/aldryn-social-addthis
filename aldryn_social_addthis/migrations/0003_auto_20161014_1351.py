# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_social_addthis', '0002_links_google'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='youtube',
            field=models.URLField(null=True, verbose_name='YouTube', blank=True),
        ),
        migrations.AlterField(
            model_name='links',
            name='facebook',
            field=models.URLField(null=True, verbose_name='Facebook', blank=True),
        ),
        migrations.AlterField(
            model_name='links',
            name='google',
            field=models.URLField(null=True, verbose_name='Google+', blank=True),
        ),
        migrations.AlterField(
            model_name='links',
            name='linkedin',
            field=models.URLField(null=True, verbose_name='LinkedIn', blank=True),
        ),
        migrations.AlterField(
            model_name='links',
            name='rss',
            field=models.URLField(null=True, verbose_name='RSS', blank=True),
        ),
        migrations.AlterField(
            model_name='links',
            name='twitter',
            field=models.URLField(null=True, verbose_name='Twitter', blank=True),
        ),
        migrations.AlterField(
            model_name='links',
            name='xing',
            field=models.URLField(null=True, verbose_name='XING', blank=True),
        ),
    ]
