import debug_toolbar
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from project_name.views import HomePageView, StyleguideView


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()

urlpatterns = patterns('',
    # See: https://docs.djangoproject.com/en/dev/topics/http/urls/

    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Homepage and styleguide
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^styleguide/', StyleguideView.as_view(), name='styleguide'),

    # Oauth2
    # url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),

    # Authentication
    url(r'^accounts/', include('registration.backends.simple.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),)
