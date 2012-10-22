from django.contrib import admin
from myproject.myapp.models import Author

AdminSite.password_change_template

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)
