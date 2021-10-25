#домашняя таблица страниц
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
]