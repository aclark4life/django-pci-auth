from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.auth.views import password_change_done
from django.contrib import admin
admin.autodiscover()


from forms import ValidatingPasswordChangeForm


urlpatterns = patterns('',
    (dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    (r'^admin/password_change/$', 'django.contrib.auth.views.password_change',
        {'password_change_form': ValidatingPasswordChangeForm}),
    (r'^admin/password_changed/$', password_change_done),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'', 'django_pci_auth.views.index'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
