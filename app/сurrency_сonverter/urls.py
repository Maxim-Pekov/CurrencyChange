from django.urls import path
from . import views

urlpatterns = [
        path('', views.Currency_converter_view.as_view()),
]