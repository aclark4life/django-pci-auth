from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import SetPasswordForm
from django.utils.translation import ugettext_lazy as _
from passwords.fields import PasswordField
from passwords.validators import validate_length, common_sequences, dictionary_words, complexity
# local
from validators import recently_used




class PasswordField(CharField):
    default_validators = [validate_length, common_sequences, dictionary_words, complexity]


class ValidatingSetPasswordForm(SetPasswordForm):
    new_password2 = PasswordField(label=_("New password confirmation"))


class ValidatingPasswordChangeForm(PasswordChangeForm):
    new_password2 = PasswordField(label=_("New password confirmation"))
