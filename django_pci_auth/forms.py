
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from django.utils.translation import ugettext_lazy as _
from passwords.fields import PasswordField
 
class ValidatingSetPasswordForm(SetPasswordForm):
    new_password2 = PasswordField(label=_("New password confirmation"))
 
class ValidatingPasswordChangeForm(PasswordChangeForm):
    new_password2 = PasswordField(label=_("New password confirmation"))



#from django import forms
#from django.conf import settings
#from django.contrib import auth
#from django.contrib.auth.hashers import check_password
#from passwords.validators import PASSWORD_MIN_LENGTH
#from models import PasswordLog
#import utils
#
#
## http://stackoverflow.com/questions/5226329/\
## enforcing-password-strength-requirements-with-django-contrib-auth-views\
## -password
#class ValidatingPasswordChangeForm(auth.forms.PasswordChangeForm):
#    """
#    Mix and match code from this StackOverflow answer and django-passwords app
#    """
#
#    MIN_LENGTH = PASSWORD_MIN_LENGTH  # Get setting from django-passwords
#
#    def clean_new_password1(self):
#        password1 = self.cleaned_data.get('new_password1')
#
#        # At least MIN_LENGTH long
##        if utils.check_password_length(password1):
#        raise forms.ValidationError(
#                "The new password must be at least %d characters long." %
#                    self.MIN_LENGTH)
#
#        # At least one letter and one non-letter
#        if not utils.check_password_complexity(password1):
#            raise forms.ValidationError(
#                "The new password must contain at least one letter and at"
#                " least one digit or punctuation character.")
#
#        # Make sure password hasn't been used recently
#        if self.user:
#            if not utils.check_password_recent(password1):
#                raise forms.ValidationError(
#                    "That password was used recently. Please pick a new one.")
#
#        return password1
