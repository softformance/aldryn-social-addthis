# -*- coding: utf-8 -*-


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
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='aldryn_social_addthis_like', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=models.deletion.CASCADE)),
                ('facebook', models.BooleanField(default=False, verbose_name='facebook')),
                ('google', models.BooleanField(default=False, verbose_name='google')),
                ('twitter', models.BooleanField(default=False, verbose_name='twitter')),
                ('pinterest', models.BooleanField(default=False, verbose_name='pinterest')),
                ('email', models.BooleanField(default=False, verbose_name='email')),
                ('title', models.CharField(default=None, max_length=255, blank=True, help_text='Uses the title of the browser window if empty.', null=True, verbose_name='title')),
                ('description', models.CharField(default=None, max_length=255, null=True, verbose_name='description', blank=True)),
                ('image', filer.fields.image.FilerImageField(blank=True, to='filer.Image', help_text='This setting can only be set once per page. If set twice, it will be overridden.', null=True, verbose_name='image', on_delete=models.SET_NULL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='aldryn_social_addthis_links', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=models.deletion.CASCADE)),
                ('facebook', models.URLField(null=True, verbose_name='facebook', blank=True)),
                ('twitter', models.URLField(null=True, verbose_name='twitter', blank=True)),
                ('xing', models.URLField(null=True, verbose_name='xing', blank=True)),
                ('linkedin', models.URLField(null=True, verbose_name='linkedin', blank=True)),
                ('rss', models.URLField(null=True, verbose_name='rss', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='aldryn_social_addthis_mail', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=models.deletion.CASCADE)),
                ('subject', models.CharField(max_length=100, verbose_name='subject')),
                ('body', models.TextField(default=b'', verbose_name='body', blank=True)),
                ('append_url', models.BooleanField(default=True, help_text='Append the current web address at the end of the mail.', verbose_name='append url')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
