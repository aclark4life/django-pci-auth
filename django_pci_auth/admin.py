from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.sites import NotRegistered
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User
from django_pci_auth.models import UserProfile, PasswordLog


# https://docs.djangoproject.com/en/1.4/topics/auth/#storing-additional-information-about-users
# Define an inline admin descriptor for UserProfile model which acts like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )


class PasswordLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'password', 'create_date')
    list_filter = ['user', 'create_date']
    search_fields = ['user', 'create_date']
    date_hierarchy = 'create_date'


try:
    admin.site.unregister(User)  # Re-register UserAdmin
except NotRegistered:
    pass  # If it's not registered, just register it (allows for custom user 
          # models)
admin.site.register(User, UserAdmin)
admin.site.register(PasswordLog, PasswordLogAdmin)

