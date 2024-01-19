from django.core.exceptions import ValidationError


def validate_price_is_positive_float(number):
    if number <= 0:
        raise ValidationError(f"The price of the object must be positive")