from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf import settings
from django.contrib import admin
from django_pci_auth.forms import ValidatingPasswordChangeForm 
admin.autodiscover()

urlpatterns = patterns('',
    (r'^doc/', include('django.contrib.admindocs.urls')),
    (r'', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
