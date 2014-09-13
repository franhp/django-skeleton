from django.conf.urls import patterns, include, url
from django.contrib import admin 
from django.views.generic.base import TemplateView
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
)
