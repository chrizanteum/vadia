from django.views.generic.base import TemplateView
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from cpu.views import CpusView, CpuView
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from motherboard.views import MotherboardsView, MotherboardView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),

    url(r'^motherboard/$', MotherboardsView.as_view(), name='motherboards_url'),
    url(r'^motherboard/(?P<pk>\d+)/$', MotherboardView.as_view(), name='motherboard_url'),

    url(r'^cpu/$', CpusView.as_view(), name='cpus_url'),
    url(r'^cpu/(?P<pk>\d+)/$', CpuView.as_view(), name='cpu_url'),
    # url(r'^is/', include('is.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
             {'document_root': settings.MEDIA_ROOT}),
    )
