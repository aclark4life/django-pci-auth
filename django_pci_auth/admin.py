from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django_pci_auth.models import UserProfile, AccessLog, PasswordLog


# https://docs.djangoproject.com/en/dev/topics/auth/#storing-additional-information-about-users
# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('attempt_time','logout_time', 'ip_address', 
        'user_agent', 'path_info')
    list_filter = ['attempt_time', 'logout_time', 'ip_address', 'path_info']
    search_fields = ['ip_address', 'user_agent', 'path_info']
    date_hierarchy = 'attempt_time'
    fieldsets = (
        (None, {
            'fields': ('path_info',)
        }),
        ('Meta Data', {
            'fields': ('user_agent', 'ip_address', 'http_accept')
        })
    )

admin.site.register(AccessLog, AccessLogAdmin)

class PasswordLogAdmin(admin.ModelAdmin):
    list_display = ('user','password', 'create_date')
    list_filter = ['user', 'create_date']
    search_fields = ['user', 'create_date']
    date_hierarchy = 'create_date'

admin.site.register(PasswordLog, PasswordLogAdmin)