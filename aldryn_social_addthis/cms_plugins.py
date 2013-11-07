# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from aldryn_social_addthis.models import Like, Mail, Links


class LikePlugin(CMSPluginBase):

    model = Like
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

    model = Mail
    name = _('Mail Plugin')

    def render(self, context, instance, placeholder):
        return context

plugin_pool.register_plugin(MailPlugin)
