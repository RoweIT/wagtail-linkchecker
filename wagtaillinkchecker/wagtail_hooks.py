from __future__ import unicode_literals

from django import __version__ as DJANGO_VERSION
from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _
from wagtail import __version__ as WAGTAIL_VERSION

from wagtaillinkchecker import urls

if DJANGO_VERSION >= '2.0':
    from django import urls as urlresolvers
else:
    from django.core import urlresolvers

if WAGTAIL_VERSION >= '2.0':
    from wagtail.admin.menu import MenuItem
    from wagtail.core import hooks
else:
    from wagtail.wagtailadmin.menu import MenuItem
    from wagtail.wagtailcore import hooks

class CustomAdminMenuItem(MenuItem):
    def is_shown(self, request):
        return request.user.is_staff


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^link-checker/', include(urls)),
    ]


@hooks.register('register_settings_menu_item')
def register_menu_settings():
    return CustomAdminMenuItem(
        _('Link Checker'),
        urlresolvers.reverse('wagtaillinkchecker'),
        classnames='icon icon-link',
        order=300
    )
