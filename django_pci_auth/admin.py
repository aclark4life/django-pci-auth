from django.contrib.admin.sites import AdminSite
from django.contrib import admin

class CustomAdmin(AdminSite):
    pass

admin_site = CustomAdmin()
