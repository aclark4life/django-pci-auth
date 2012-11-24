from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.conf import settings

from models import PasswordLog, UserProfile

# django 1.4 has a new timezone aware now() use if available.
try:
    from django.utils.timezone import now
except ImportError:
    # fall back to none timezone aware now()
    from datetime import datetime
    now = datetime.now


OLD_PASSWORD_STORAGE_NUM = getattr(settings, "OLD_PASSWORD_STORAGE_NUM", 4)

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
    user_profile.password_last_changed = now()  #need to handle timezone
    user_profile.save()

    # log the password change
    password_log = PasswordLog()
    password_log.user = user
    password_log.password = user.password
    password_log.create_date = now()
    password_log.save()

    # expire old used passwords (move someone else?)
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