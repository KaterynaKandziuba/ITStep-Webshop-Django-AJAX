#домашняя таблица страниц
from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
]