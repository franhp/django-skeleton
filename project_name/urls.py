import debug_toolbar
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from project_name.views import HomePageView


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()

urlpatterns = patterns('',
    # See: https://docs.djangoproject.com/en/dev/topics/http/urls/

    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    # Homepage
    url(r'^$', HomePageView.as_view(), name='home'),
    
    # Oauth2
    # url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),)
