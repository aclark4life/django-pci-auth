from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    nolockout = models.BooleanField()
