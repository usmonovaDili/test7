from django.core.exceptions import ValidationError
from django.core.validators import validate_email as email_validate


def validate_email(value: str):
    msg = 'yaroqli email kiriting'

    if not value:
        return False, msg
    try:
        email_validate(value)
    except ValidationError:
        return True, ''

