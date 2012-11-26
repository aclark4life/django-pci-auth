from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
import signals

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    nolockout = models.BooleanField()
    password_last_changed = models.DateTimeField(auto_now_add=True)

class PasswordLog(models.Model):
    user = models.ForeignKey(User)
    password = models.CharField(_('password'), max_length=128)
    create_date = models.DateTimeField(_('Create Date'), auto_now_add=True)

    def __unicode__(self):
        return u'Password log for %s @ %s' % (self.user, self.create_date)

    class Meta:
        ordering = ['-create_date']