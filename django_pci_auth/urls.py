
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.auth.views import password_change_done

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


from forms import ValidatingPasswordChangeForm


urlpatterns = patterns('',
    # Example:
    # (r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),
    (r'^admin/password_change/$', 'django.contrib.auth.views.password_change', {'password_change_form': ValidatingPasswordChangeForm}),
    (r'^admin/password_changed/$', password_change_done),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),



    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Hello, world!
    (r'', 'django_pci_auth.views.index'),




)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )



#from dajaxice.core import dajaxice_autodiscover, dajaxice_config
#from django.conf.urls.defaults import *
#from django.conf import settings
#from django.contrib.auth.views import password_change
#from django.contrib import admin
#from django_pci_auth.views import index, password_change_done
#from django_pci_auth.forms import ValidatingPasswordChangeForm
#import django.contrib.admindocs.urls
#
#
#admin.autodiscover()
#dajaxice_autodiscover()
#
#
#urlpatterns = patterns(
#    '',  # prefix
#    (r'^admin/doc/', include(django.contrib.admindocs.urls)),
#    (r'^admin/', include(admin.site.urls)),
#    (r'^change_password/$', password_change,
#        {'password_change_form': ValidatingPasswordChangeForm,
#        'post_change_redirect' : '/password_changed/'}),
#    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
#    (r'^password_changed/$', password_change_done),
#    (r'', index),
#)
#
#if settings.DEBUG:
#    urlpatterns += patterns(
#        '',
#        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
#            {'document_root': settings.MEDIA_ROOT}),

#    )
