# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.templatetags.static import static

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
    render_template = 'aldryn_social_addthis/plugins/mail.html'

    def render(self, context, instance, placeholder):
        return context

plugin_pool.register_plugin(MailPlugin)


class LinksPlugin(CMSPluginBase):

    model = Links
    name = _('Social links')
    render_template = 'aldryn_social_addthis/plugins/links.html'
    ICON_URL = 'aldryn_social_addthis/icons/%(network)s_link.png'

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        links = []
        for network_name in Links.AVAILABLE_LINKS:
            social_url = getattr(instance, network_name)
            if social_url:
                icon_url = static(self.ICON_URL % {'network': network_name})
                links.append((network_name, social_url, icon_url))
        context['links'] = links
        return context

plugin_pool.register_plugin(LinksPlugin)
