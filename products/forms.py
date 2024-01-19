from django import forms
from django.contrib.auth import get_user_model

from core.form_mixins import DisabledFormMixin
from products.models import Product

UserModel = get_user_model()


class ProductBaseForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'release_date', 'personal_photo')
        labels = {
            'name': 'Pet Name',
            'personal_photo': 'Link to Image',
            'date_of_birth': 'Date of Birth'
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet Name',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd//yyyy',
                    'type': 'date',
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to Image',
                }
            )
        }


class ProductCreateForm(ProductBaseForm):
    pass


class PetEditForm(ProductBaseForm):
    pass


class PetDeleteForm(DisabledFormMixin, ProductBaseForm):
    disabled_fields = ('name', 'release_date', 'personal_photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            pass
        return self.instance
