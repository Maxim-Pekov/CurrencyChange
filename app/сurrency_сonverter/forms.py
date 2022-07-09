from django import forms
from .models import Currency_converter


class Currency_converter_form(forms.ModelForm):
    class Meta:
        model = Currency_converter
        fields =  ['currency_quality']
        labels = {
            'currency_quality' : 'Кол-во валюты'
        }
        error_messages = {  # Какие сообщения будут при ошибках ввода в формы
            'currency_quality' : {
                'required': 'Введите имя',     #Ошибки если не ввели данные
                'min_lenght': 'Введите больше 1 символа',
                'max_length': f'Введите меньше 5'
            }
        }