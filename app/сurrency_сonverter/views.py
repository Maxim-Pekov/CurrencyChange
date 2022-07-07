from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from . import forms
from .models import Currency_converter
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView


class Currency_converter_view(CreateView):
    model = Currency_converter
    template_name = 'сurrency_сonverter/index.html'
    form_class = forms.Currency_converter_form
    success_url = '/index.html'
