from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import SetPasswordForm
from django.forms import ValidationError
from django.utils.translation import ugettext_lazy as _
from passwords.fields import PasswordField
from django_pci_auth.models import PasswordLog


def check_password_recent(user, password1):
    # Make sure password hasn't been used recently
    p_logs = PasswordLog.objects.filter(user=user)
    for p_log in p_logs:
        if not check_password(password1, p_log.password):
            return False
    return True


class PCICompliantPasswordField(PasswordField):
    """
    """


class ValidatingSetPasswordForm(SetPasswordForm):
    new_password2 = PCICompliantPasswordField(label=_("New password confirmation"))


class ValidatingPasswordChangeForm(PasswordChangeForm):
    new_password2 = PCICompliantPasswordField(label=_("New password confirmation"))

    def clean_new_password2(self):
        password2 = self.cleaned_data.get('new_password2')

        # Make sure password hasn't been used recently
        if self.user:
            user = self.user
            if not check_password_recent(user, password2):
                raise ValidationError(
                    "That password was used recently. Please pick a new one.")
        return password2
