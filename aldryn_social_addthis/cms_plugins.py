# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.templatetags.static import static

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from aldryn_social_addthis import models as plugin_models


class LikePlugin(CMSPluginBase):

    model = plugin_models.Like
    name = _('Share Button')
    render_template = 'aldryn_social_addthis/plugins/like.html'

    fieldsets = [
        (
            None,
            {'fields': ['facebook', 'google', 'twitter', 'pinterest', 'email']}
        ),
        (
            _('Advanced'),
            {'fields': ['title', 'description', 'image']}
        ),
    ]

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['placeholder'] = placeholder
        if instance.image_id:
            r = context['request']
            context['image_url'] = '%s://%s%s' % ('https' if r.is_secure() else 'http', r.get_host(), instance.image.url)
        return context

plugin_pool.register_plugin(LikePlugin)


class MailPlugin(CMSPluginBase):

    model = plugin_models.Mail
    name = _('Mail Plugin')
    render_template = 'aldryn_social_addthis/plugins/mail.html'

    def render(self, context, instance, placeholder):
        return context

plugin_pool.register_plugin(MailPlugin)


class LinksPlugin(CMSPluginBase):

    model = plugin_models.Links
    name = _('Social links')
    render_template = 'aldryn_social_addthis/plugins/links.html'

    ICON_URL = 'aldryn_social_addthis/icons/%(network)s_link.png'

    def get_fieldsets(self, request, obj=None):
        networks = list(plugin_models.AVAILABLE_NETWORKS)
        networks_by_name = dict(plugin_models.SOCIAL_NETWORKS_BY_NAME)
        fieldsets = [(networks_by_name[network], {'fields': [network]}) for network in networks]
        return fieldsets

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['networks'] = instance.get_links()
        return context

plugin_pool.register_plugin(LinksPlugin)
