# additional django-passwords validators
from django.contrib.auth.hashers import check_password
from django.utils.translation import ugettext_lazy as _
# local
from models import PasswordLog


class RecentlyUsedValidator(object):
    message = _("Recently used (%s)")
    code = "recently_used"

    def __init__(self):
        self.user = user

    def __call__(self, user, password):
        # Make sure password hasn't been used recently
        p_logs = PasswordLog.objects.filter(user=user)
        for p_log in p_logs:
            if not check_password(password, p_log.password):
                raise ValidationError(
                    self.message % _("Must not be used recently"), 
                    code=self.code)


recently_used = RecentlyUsedValidator()
