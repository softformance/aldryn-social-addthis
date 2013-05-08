# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from aldryn_social_sharing.models import Like, Mail, Links


class LikePlugin(CMSPluginBase):

    model = Like
    name = _('Like Plugin')
    render_template = 'aldryn_social_sharing/plugins/like.html'

    module = 'Social'

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
    render_template = 'aldryn_social_sharing/plugins/mail.html'

    module = 'Social'

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['subject'] = instance.subject.replace(' ', '%20')
        context['body'] = instance.body.replace(' ', '%20')
        return context

plugin_pool.register_plugin(MailPlugin)


class LinksPlugin(CMSPluginBase):

    model = Links
    name = _('Links')
    render_template = 'aldryn_social_sharing/plugins/links.html'

    module = 'Social'

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['links'] = {}
        for link in instance.links:
            value = getattr(instance, link, False)
            if value:
                context['links'][link] = value
        return context

plugin_pool.register_plugin(LinksPlugin)
