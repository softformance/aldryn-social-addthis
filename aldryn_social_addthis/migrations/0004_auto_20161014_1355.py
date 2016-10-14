# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_social_addthis', '0003_auto_20161014_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='instagram',
            field=models.URLField(null=True, verbose_name='Instagram', blank=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_social_addthis_like', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='links',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_social_addthis_links', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_social_addthis_mail', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
