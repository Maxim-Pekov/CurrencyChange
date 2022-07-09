from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Currency_converter
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
import requests, os
from bs4 import BeautifulSoup as b
from datetime import datetime
import time
from .forms import Currency_converter_form

class Currency_converter_view(FormView):
    success_url = '/'
    amount = 0
    from_cur = ''
    to_cur = ''
    def get(self, request):
        form = Currency_converter_form()
        context = {
            'currency_codes': Currency_converter.objects.all()
        }
        return render(request, 'сurrency_сonverter/index.html', context=context)

    def post(self, request):
        # form = Currency_converter_form(request.POST)  # Instanse -говорит что данные уже есть
        self.amount = request.POST.get('amount')
        self.from_cur = request.POST.get('from_curr')
        self.to_cur = request.POST.get('to_curr')
        dict = parser()
        dict_from_curr = dict[self.from_cur]
        dict_to_curr = dict[self.to_cur]
        convert_amount = round((int(dict_from_curr[0]) * float((dict_from_curr[2]).replace(',','.'))) / int(dict_to_curr[0]), 2)
        context = {
            'currency_codes': parser().keys(),
            'amount': self.amount,
            'from_cur': self.from_cur,
            'to_cur': self.to_cur,
            'convert_amount': convert_amount
        }
        return render(request, 'сurrency_сonverter/index.html', context=context)


URL = 'http://www.cbr.ru/currency_base/daily/'


def copy_url_by_text():
    date_now = round(time.time() / 60 / 60 / 24)
    date_change_file = round(
        (os.path.getmtime('сurrency_сonverter/static/сurrency_сonverter/file/currency.html')) / 60 / 60 / 24)
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    if date_change_file != date_now:
        r = requests.get(URL, headers=headers)
        src = r.text
        with open('сurrency_сonverter/static/сurrency_сonverter/file/currency.html', 'w') as file:
            file.write(src)


def parser():
    copy_url_by_text()
    with open('сurrency_сonverter/static/сurrency_сonverter/file/currency.html') as file:
        SRC = file.read()
    soup = b(SRC, 'lxml')
    currency = soup.find_all('tr')
    count = 0
    currency_code = []
    currency_dict = {}
    for t in currency:
        x = t.find_all('td')
        if count > 0:
            curr = x[1].text
            currency_code.append(x[1].text)
            currency_dict[curr] = [x[2].text, x[3].text, x[4].text]
            # cur = Currency_converter(
            #     currency_code=f'{x[1].text}',
            #     currency_quality=f'{x[2].text}',
            #     currency_name=f'{x[3].text}',
            #     currency_curs_by_rub=(f'{x[4].text}').replace(',', '.')
            # )
            # cur.save()
            # print(curr)
        count += 1
    return currency_dict

# list_of_clear_anekdot = parser(URL)
