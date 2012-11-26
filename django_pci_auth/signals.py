from django.conf import settings
from django.core.mail import send_mail
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.dispatch import receiver
from django.contrib.auth import get_user
from axes.signals import user_locked_out

@receiver(user_locked_out)
def send_lockout_email(sender, request, username, ip_address, signal, *args, **kwargs):
    """ If the user getting locked out is a real account, 
    email them and let them know """
    user = get_user(request)
    # if the user is anonymous then no need to send email
    if not user.is_anonymous():
        current_site = Site.objects.get_current()
        subject = "Password Reset on %(site_name)s" % {
                'site_name': current_site.name
            }
        message = render_to_string( 'account/locked_out_email.txt', {
            'username': username,
            'ip_address': ip_address,
            'current_site': current_site
        })
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])