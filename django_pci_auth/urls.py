from django.conf.urls import patterns, url, include
from django_pci_auth import views

urlpatterns = patterns('',
    (r'', views.current_datetime),
)
