from django import forms
from django.forms.widgets import DateInput
from products.models import Batch
from datetime import date


class BatchForm(forms.ModelForm):
    """Generates form to create and update batches"""

    class Meta:
        model = Batch
        fields = ['product', 'batch_number', 'expiry_date', 'quantity',
                  'offer', 'discount_percentage']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['expiry_date'].widget = DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'min': date.today().strftime('%Y-%m-%d'),
        })

    def check_discount_percentage(self):
        """Makes discount_percentage mandatory if `offer = 2`"""
        offer = self.cleaned_data.get('offer')
        discount_percentage = self.cleaned_data.get('discount_percentage')

        if discount_percentage is not None:
            if discount_percentage <= 0 or discount_percentage >= 100:
                raise forms.ValidationError(
                    "Discount percentage must be"
                    "greater than 0 and less than 100.")

        return discount_percentage

    def check_expiry_date(self):
        """Only allows user to set expiry date to a future date"""
        expiry_date = self.cleaned_data.get('expiry_date')
        if expiry_date:
            if expiry_date <= date.today():
                raise forms.ValidationError(
                    "The expiry date must be in the future."
                )
        else:
            raise forms.ValidationError(
                "Expiry date is required and must be a future date."
            )

        return expiry_date


class BatchDiscountForm(forms.ModelForm):
    """Applies a discount to a Batch"""

    class Meta:
        model = Batch
        fields = ['discount_percentage']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_discount_percentage(self):
        """
        Sets Discount percentage to be greater than 0 and lesser than 100.
        """
        discount_percentage = self.cleaned_data.get('discount_percentage')

        if discount_percentage is None:
            raise forms.ValidationError("Discount percentage is required.")

        if discount_percentage <= 0 or discount_percentage >= 100:
            raise forms.ValidationError("Discount percentage must be"
                                        "greater than 0 and lesser than 100.")

        return discount_percentage
