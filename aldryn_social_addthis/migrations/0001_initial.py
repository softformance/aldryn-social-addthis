# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('facebook', models.BooleanField(default=False, verbose_name='facebook')),
                ('google', models.BooleanField(default=False, verbose_name='google')),
                ('twitter', models.BooleanField(default=False, verbose_name='twitter')),
                ('pinterest', models.BooleanField(default=False, verbose_name='pinterest')),
                ('email', models.BooleanField(default=False, verbose_name='email')),
                ('title', models.CharField(default=None, max_length=255, blank=True, help_text='Uses the title of the browser window if empty.', null=True, verbose_name='title')),
                ('description', models.CharField(default=None, max_length=255, null=True, verbose_name='description', blank=True)),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='aldryn_social_addthis_like', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('image', filer.fields.image.FilerImageField(blank=True, to='filer.Image', help_text='This setting can only be set once per page. If set twice, it will be overridden.', null=True, verbose_name='image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('facebook', models.URLField(null=True, verbose_name='Facebook', blank=True)),
                ('instagram', models.URLField(null=True, verbose_name='Instagram', blank=True)),
                ('google', models.URLField(null=True, verbose_name='Google+', blank=True)),
                ('twitter', models.URLField(null=True, verbose_name='Twitter', blank=True)),
                ('youtube', models.URLField(null=True, verbose_name='YouTube', blank=True)),
                ('xing', models.URLField(null=True, verbose_name='XING', blank=True)),
                ('linkedin', models.URLField(null=True, verbose_name='LinkedIn', blank=True)),
                ('rss', models.URLField(null=True, verbose_name='RSS', blank=True)),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='aldryn_social_addthis_links', primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('subject', models.CharField(max_length=100, verbose_name='subject')),
                ('body', models.TextField(default=b'', verbose_name='body', blank=True)),
                ('append_url', models.BooleanField(default=True, help_text='Append the current web address at the end of the mail.', verbose_name='append url')),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='aldryn_social_addthis_mail', primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
