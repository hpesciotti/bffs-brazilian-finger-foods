from django import forms
from products.models import Product, Batch, DietaryCategory

class BatchForm(forms.ModelForm):
    """Generates form to create and update batches"""
    
    class Meta:
        model = Batch
        fields = ['product', 'batch_number', 'expiry_date', 'quantity', 
                  'offer', 'discount_percentage', 'sale_price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def check_discount_percentage(self):
        """Makes discount_percentage mandatory if `offer = 2`"""
        offer = self.cleaned_data.get('offer')
        discount_percentage = self.cleaned_data.get('discount_percentage')

        if offer == 2 and (discount_percentage is None or discount_percentage <= 0):
            raise forms.ValidationError(
                "Discount percentage is required and must be greater than 0 when an offer is set."
            )

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