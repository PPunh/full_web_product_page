# coding=utf-8
from django import forms

#Models
from .models import ProductsModel, ProductsCategory

class ProductsCategoryModelForm(forms.ModelForm):
    class Meta:
        model = ProductsCategory
        exclude = ('category_id',)
    
    def __init__(self, *args, **kwargs):
        super(ProductsCategoryModelForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control w3-input w3-border w3-round w3-margin-bottom'

# ProducrModel 
class ProductsModelForm(forms.ModelForm):
    class Meta:
        model = ProductsModel
        exclude = ('product_id',)


    def __init__(self, *args, **kwargs):
        super(ProductsModelForm, self).__init__(*args, **kwargs) 

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control w3-input w3-border w3-round w3-margin-bottom'

            if isinstance(field, forms.DateField):
                field.widget = forms.DateInput(attrs={
                    'class': 'form-control w3-input w3-border w3-round w3-margin-bottom',
                    'type':'date'
                })