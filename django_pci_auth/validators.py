# additional django-passwords validators
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
# local
from models import PasswordLog


class RecentlyUsedValidator(object):
    message = _("Recently used (%s)")
    code = "recently_used"

    def __call__(self, value):
        # Make sure password hasn't been used recently
        p_logs = PasswordLog.objects.filter(user=1)  # XXX Need real user
        for p_log in p_logs:
            if not check_password(value, p_log.password):
                raise ValidationError(
                    self.message % _("Must not be recently used"),
                    code=self.code)


recently_used = RecentlyUsedValidator()
