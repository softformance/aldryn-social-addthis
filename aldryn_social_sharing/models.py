# -*- coding: utf-8 -*-
from django.db import models
from django.template import Context
from django.template.loader import get_template
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField

from aldryn_social_sharing import defaults


class Like(CMSPlugin):

    facebook = models.BooleanField(_('facebook'), default=False)
    google = models.BooleanField(_('google'), default=False)
    twitter = models.BooleanField(_('twitter'), default=False)
    pinterest = models.BooleanField(_('pinterest'), default=False)
    email = models.BooleanField(_('email'), default=False)

    buttons = [
        ('facebook', 'aldryn_social_sharing/likes/facebook.html'),
        ('google', 'aldryn_social_sharing/likes/google.html'),
        ('twitter', 'aldryn_social_sharing/likes/twitter.html'),
        ('pinterest', 'aldryn_social_sharing/likes/pinterest.html'),
        ('email', 'aldryn_social_sharing/likes/email.html')]

    title = models.CharField(
        _('title'),
        max_length=255,
        default=defaults.LIKE['title'],
        blank=True,
        null=True,
        help_text=_('Uses the title of the browser window if empty.'))
    description = models.CharField(
        _('description'),
        max_length=255,
        default=defaults.LIKE['description'],
        blank=True,
        null=True)
    image = FilerImageField(
        verbose_name=_('image'),
        blank=True,
        null=True,
        help_text=_('This setting can only be set once per page. If set twice, it will be overridden.'))

    def get_buttons(self):
        context = Context({'title': self.title,
                           'description': self.description})
        for button, template_path in self.buttons:
            if getattr(self, button):
                template = get_template(template_path)
                yield template.render(context)


class Mail(CMSPlugin):

    subject = models.CharField(_('subject'), max_length=100)
    body = models.TextField(_('body'), default='', blank=True)
    append_url = models.BooleanField(
        _('append url'),
        default=True,
        help_text=_('Append the current web address at the end of the mail.'))


class Links(CMSPlugin):

    facebook = models.URLField(_('facebook'), null=True, blank=True)
    twitter = models.URLField(_('twitter'), null=True, blank=True)
    xing = models.URLField(_('xing'), null=True, blank=True)
    linkedin = models.URLField(_('linkedin'), null=True, blank=True)
    rss = models.URLField(_('rss'), null=True, blank=True)

    links = ['facebook', 'twitter', 'xing', 'linkedin', 'rss']
