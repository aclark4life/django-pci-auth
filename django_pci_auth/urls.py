from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf import settings
from django.contrib import admin
from django_pci_auth.views import index
import django.contrib.admindocs.urls


admin.autodiscover()


urlpatterns = patterns(
    '',  # prefix
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include(django.contrib.admindocs.urls)),
    (r'', index),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
