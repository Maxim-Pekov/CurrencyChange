from django import forms
from .models import Currency_converter


class Currency_converter_form(forms.ModelForm):
    class Meta:
        model = Currency_converter
        fields = '__all__'
