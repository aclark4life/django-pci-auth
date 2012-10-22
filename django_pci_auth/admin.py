from django.contrib.admin.sites import AdminSite

class CustomAdmin(AdminSite):
    pass

admin_site = CustomAdmin()
