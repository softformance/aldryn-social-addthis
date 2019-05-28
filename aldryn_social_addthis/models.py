# -*- coding: utf-8 -*-
from collections import OrderedDict
from functools import partial

from django.db import models
from django.conf import settings
from django.template.loader import get_template
from django.templatetags.static import static
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin

from filer.fields.image import FilerImageField

from aldryn_social_addthis import defaults


SOCIAL_NETWORKS = (
    ('facebook', _('Facebook')),
    ('instagram', _('Instagram')),
    ('twitter', _('Twitter')),
    ('youtube', _('YouTube')),
    ('xing', _('XING')),
    ('linkedin', _('LinkedIn')),
    ('rss', _('RSS')),
)

SOCIAL_NETWORKS_BY_NAME = OrderedDict(SOCIAL_NETWORKS)

AVAILABLE_NETWORKS = getattr(settings, 'ALDRYN_SOCIAL_ADDTHIS_NETWORKS', list(SOCIAL_NETWORKS_BY_NAME.keys()))

CMSPluginField = partial(
    models.OneToOneField,
    to=CMSPlugin,
    related_name='%(app_label)s_%(class)s',
    parent_link=True,
    on_delete=models.deletion.CASCADE
)


class Like(CMSPlugin):

    facebook = models.BooleanField(_('facebook'), default=False)
    twitter = models.BooleanField(_('twitter'), default=False)
    pinterest = models.BooleanField(_('pinterest'), default=False)
    email = models.BooleanField(_('email'), default=False)

    buttons = [
        ('facebook', 'aldryn_social_addthis/likes/facebook.html'),
        ('twitter', 'aldryn_social_addthis/likes/twitter.html'),
        ('pinterest', 'aldryn_social_addthis/likes/pinterest.html'),
        ('email', 'aldryn_social_addthis/likes/email.html')
    ]

    title = models.CharField(
        verbose_name=_('title'),
        max_length=255,
        default=defaults.LIKE['title'],
        blank=True,
        null=True,
        help_text=_('Uses the title of the browser window if empty.')
    )
    description = models.CharField(
        verbose_name=_('description'),
        max_length=255,
        default=defaults.LIKE['description'],
        blank=True,
        null=True
    )
    image = FilerImageField(
        verbose_name=_('image'),
        blank=True,
        null=True,
        help_text=_('This setting can only be set once per page. If set twice, it will be overridden.'),
        on_delete=models.SET_NULL,
    )
    cmsplugin_ptr = CMSPluginField()

    def get_buttons(self):

        context = {
            'title': self.title,
            'description': self.description,
            'image_url': self.image.url if self.image else None
        }
        for button, template_path in self.buttons:
            if getattr(self, button):
                template = get_template(template_path)
                yield template.render(context)


class Mail(CMSPlugin):

    subject = models.CharField(_('subject'), max_length=100)
    body = models.TextField(_('body'), default='', blank=True)
    append_url = models.BooleanField(
        verbose_name=_('append url'),
        default=True,
        help_text=_('Append the current web address at the end of the mail.')
    )
    cmsplugin_ptr = CMSPluginField()


class Links(CMSPlugin):

    facebook = models.URLField(_('Facebook'), null=True, blank=True)
    instagram = models.URLField(_('Instagram'), null=True, blank=True)
    twitter = models.URLField(_('Twitter'), null=True, blank=True)
    youtube = models.URLField(_('YouTube'), null=True, blank=True)
    xing = models.URLField(_('XING'), null=True, blank=True)
    linkedin = models.URLField(_('LinkedIn'), null=True, blank=True)
    rss = models.URLField(_('RSS'), null=True, blank=True)
    cmsplugin_ptr = CMSPluginField()

    def get_link(self, network):
        icon_path = self.get_plugin_class().ICON_URL % {'network': network}
        return {'name': network, 'url': getattr(self, network), 'icon_url': static(icon_path)}

    def get_links(self):
        return [self.get_link(network) for network in AVAILABLE_NETWORKS if getattr(self, network)]
