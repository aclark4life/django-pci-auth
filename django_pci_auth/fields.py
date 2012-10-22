# Dress up django-passwords imports to make avail as django_pci_auth.fields
from passwords.fields import PasswordField as _PasswordField
PasswordField = _PasswordField
