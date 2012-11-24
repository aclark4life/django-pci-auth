from django import forms
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.hashers import check_password
from passwords.validators import PASSWORD_MIN_LENGTH
from models import PasswordLog

# http://stackoverflow.com/questions/5226329/\
# enforcing-password-strength-requirements-with-django-contrib-auth-views\
# -password
class ValidatingPasswordChangeForm(auth.forms.PasswordChangeForm):
    """
    Mix and match code from this StackOverflow answer and django-passwords app
    """

    MIN_LENGTH = PASSWORD_MIN_LENGTH  # Get setting from django-passwords

    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')

        # At least MIN_LENGTH long
        if len(password1) < self.MIN_LENGTH:
            raise forms.ValidationError(
                "The new password must be at least %d characters long." %
                    self.MIN_LENGTH)

        # At least one letter and one non-letter
        first_isalpha = password1[0].isalpha()
        if all(c.isalpha() == first_isalpha for c in password1):
            raise forms.ValidationError(
                "The new password must contain at least one letter and at"
                " least one digit or punctuation character.")

        # ... any other validation you want ...
        if self.user:
            # Make sure password hasn't been used recently
            p_logs = PasswordLog.objects.filter(user=self.user)
            for p_log in p_logs:
                if check_password(password1, p_log.password):
                    raise forms.ValidationError(
                    "That password was used recently. Please pick a new one.")

        return password1
