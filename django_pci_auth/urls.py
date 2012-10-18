from django.contrib import admin
from django.conf.urls import include, patterns, url
from django_pci_auth import views

urlpatterns = patterns('',
    (r'', include(admin.site.urls)),
)
