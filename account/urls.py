# домашняя таблица страниц
from django.urls import path
from .views import ajax_reg, register, entry, sign_out

# маршрутизатор - это по сути список маршрутов
urlpatterns = [
    path('register', register), # маскировка - вместо 'register' написать 'route1'
    path('entry', entry),
    path('logout', sign_out),
    path('ajax_reg', ajax_reg)    
]