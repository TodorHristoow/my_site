from django.contrib.auth import get_user_model
from django.db import models
from django.core import validators
from django.utils.text import slugify

from core.model_mixin import StrFromFieldsMixin
from products.validators import validate_price_is_positive_float

UserModel = get_user_model()


class Product(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name')

    name = models.CharField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=
        (
            validate_price_is_positive_float,
        )
    )

    description = models.TextField(
        null=True,
        blank=True,
        max_length=255)

    personal_photo = models.URLField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    release_date = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    def save(self, *args, **kwargs):
        # Create/Update so it generates and id
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')
        # Update with generated id
        return super().save(*args, **kwargs)
