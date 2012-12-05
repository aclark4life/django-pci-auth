from django.core.exceptions import ValidationError
from forms import PCICompliantPasswordField
import sys


def validate_field(password):
    errors = ""
    # XXX A better way to validate here?
    field = PCICompliantPasswordField()
    for validator in field.validators:
        try:
            validator(password)
        except ValidationError:
            error = sys.exc_info()[1]
            if errors != "":  # Add sep
                errors += '</span><span class="alert alert-error">'
            errors += error.__dict__['messages'][0]  # XXX Srsly?
    return errors
