from django.contrib import admin
from django_pci_auth import urls

ROOT_URLCONF = urls
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase'
    }
}
DEBUG = True

admin.autodiscover()
