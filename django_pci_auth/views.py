from dajaxice.decorators import dajaxice_register
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
import json

# django 1.4 has a new timezone aware now() use if available.
try:
    from django.utils.timezone import now
except ImportError:
    # fall back to none timezone aware now()
    from datetime import datetime
    now = datetime.now
# local
from models import PasswordLog
from models import UserProfile
from utils import validate_field


# XXX Can we get the "real" message string from somewhere?
BAD_PASS_MSG = ('Your old password was entered incorrectly. '
    'Please enter it again.')
NOT_EQUAL_MSG = ('Passwords are not equal. '
    '(Passwords must be equal)')

OLD_PASSWORD_STORAGE_NUM = getattr(settings, "OLD_PASSWORD_STORAGE_NUM", 4)
PASSWORD_MIN_LENGTH = str(getattr(settings, "PASSWORD_MIN_LENGTH", ''))


def index(request):
    return render_to_response('django_pci_auth.html')


# taken and altered from django.contrib.auth.views.password_change_done to add
# code for logging password changes.
@login_required
def password_change_done(request,
    template_name='registration/password_change_done.html',
    current_app=None, extra_context=None):

    # update the password last changed date on profile.
    user = request.user
    try:
        user_profile = user.get_profile()
    except UserProfile.DoesNotExist:
        user_profile = UserProfile()
        user_profile.user = user
    user_profile.password_last_changed = now()  # need to handle timezone
    user_profile.save()

    # log the password change
    password_log = PasswordLog()
    password_log.user = user
    password_log.password = user.password
    password_log.create_date = now()
    password_log.save()

    # expire old used passwords (move somewhere else?)
    p_logs = PasswordLog.objects.filter(user=user).order_by("-create_date")
    p_count = 0
    for p_log in p_logs:
        p_count += 1
        if p_count < (OLD_PASSWORD_STORAGE_NUM + 1):
            continue
        # remove the oldest logs over our storage limit.
        p_log.delete()

    # original stuff below.
    context = {}
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)


@dajaxice_register
def check_setting_password_length(request):
    return json.dumps({'message': PASSWORD_MIN_LENGTH})


@dajaxice_register
def check_old_password(request, password):
    user = User.objects.get(username__exact=request.user)
    results = user.check_password(password)
    if results:
        results = '<span class="alert alert-success">OK</span>'
    else:
        results = '<span class="alert alert-error">%s</span>' % BAD_PASS_MSG
    return json.dumps({'message': results})


@dajaxice_register
def check_new_password1(request, password):
    errors = validate_field(password)
    if not errors:
        results = '<span class="alert alert-success">OK</span>'
    else:
        results = '<span class="alert alert-error">%s</span>' % errors
    return json.dumps({'message': results})


@dajaxice_register
def check_new_password2(request, password):
    password1 = password2 = None
    if 'new_password1' in password:
        password1 = password['new_password1']
    if 'new_password2' in password:
        password2 = password['new_password2']
    errors1 = validate_field(password1)
    errors2 = validate_field(password2)
    equal = password1 == password2
    if equal and not errors1 and not errors2:
        results = '<span class="alert alert-success">OK</span>'
    else:
        if not equal:
            errors2 += ('<span class="alert alert-error">%s</span>' %
                NOT_EQUAL_MSG)
        results = '<span class="alert alert-error">%s</span>' % errors2
    return json.dumps({'message': results})
