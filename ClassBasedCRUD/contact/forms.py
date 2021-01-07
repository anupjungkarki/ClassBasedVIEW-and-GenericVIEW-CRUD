from django import forms
from .models import Product

# Talako Sabai Form lai Deign Dina Matra hO kasai Khi haina Yo ni one method of form designe garne
class ProductForms(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Enter Your Title'}),
                            required=True, max_length=100)

    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                    'placeholder': 'Enter Your Description'}),
                                  required=True, max_length=1000)

    price = forms.CharField(label='Price', widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'Enter Your Price'}),
                                  required=True, max_length=200)

    class Meta:
        model = Product
        fields = "__all__"
