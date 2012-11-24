from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    nolockout = models.BooleanField()
    password_last_changed = models.DateTimeField(auto_now_add=True)

class AccessLog(models.Model):
    user_agent = models.CharField(max_length=255)
    ip_address = models.IPAddressField('IP Address', null=True)
    user = models.ForeignKey(User)
    trusted = models.BooleanField(default=False)
    http_accept = models.CharField('HTTP Accept', max_length=255)
    path_info = models.CharField('Path', max_length=255)
    attempt_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return u'Attempted Access for %s @ %s' % (self.user, self.attempt_time)

    class Meta:
        ordering = ['-attempt_time']

class PasswordLog(models.Model):
    user = models.ForeignKey(User)
    password = models.CharField(_('password'), max_length=128)
    create_date = models.DateTimeField(_('Create Date'), auto_now_add=True)

    def __unicode__(self):
        return u'Password log for %s @ %s' % (self.user, self.create_date)

    class Meta:
        ordering = ['-create_date']