from django.contrib.auth.hashers import check_password
from models import PasswordLog
from passwords.validators import PASSWORD_MIN_LENGTH


def check_password_length(password1):
    # At least MIN_LENGTH long
    results = len(password1) < PASSWORD_MIN_LENGTH  # Get setting from django-passwords
    return results


def check_password_complexity(password1):
    # At least one letter and one non-letter
    first_isalpha = password1[0].isalpha()
    results = all(c.isalpha() == first_isalpha for c in password1)
    return results


def check_password_recent(user, password1):
    # Make sure password hasn't been used recently
    p_logs = PasswordLog.objects.filter(user=user)
    for p_log in p_logs:
        if not check_password(password1, p_log.password):
            return False
    return True
