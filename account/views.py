from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

# Каждый вид определяет сценарий загрузки шаблона
# Мы не используем термин контроллер, потому что используем архитектурный паттерн
# MVT - model view template


def register(request):
    if request.method == 'GET':
        return render(request, 'account/register.html', context={
            'page_name': 'Регистрация',
            'page_app': 'account',
            'page_view': 'register'
        })  # данные транзитно передаются с вьюхи в контекст
# returns http response
# но сам вызов вида (вьюхи) происходит через маршрутизатор
# router - view - template
    elif request.method == 'POST':
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        pass2_x = request.POST.get('pass2')
        email_x = request.POST.get('email')

# 1 - Валидация данных (на стороне сервера) ...
# 2 - Сохранение пользователя в базе данных ...
    user = User.objects.create_user(login_x, email_x, pass1_x)
    if user is None:
        mess = 'В регистрации отказано!'
        color = 'red'
    else:
        user.save()
        mess = 'Регистрация успешно завершена!'
        color = 'green'

# 3 - Вывод отчета ...
        return render(request, 'account/report.html', context={
            'page_name': 'Отчет о регистрации',
            'page_app': 'account',
            'page_view': 'report',
            'mess': mess,
            'color': color
        })


def entry(request):
    if request.method == 'GET':
        return render(request, 'account/entry.html', context={
            'page_name': 'Авторизация',
            'page_app': 'account',
            'page_view': 'entry'
        })
    elif request.method == 'POST':
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
    # Проверка подлинности пары логин - пароль
    # автоматически хеширует пароль
    user = authenticate(request, username=login_x, password=pass1_x)
    if user is None:
        mess = 'Пользователь не найден!'
        color = 'red'
        return render(request, 'account/report.html', context={
            'page_name': 'Отчет об авторизации',
            'page_app': 'account',
            'page_view': 'report',
            'mess': mess,
            'color': color
        })
    else:
        login(request, user)  # функция регистрирует пользователя в сеансе связи
        return redirect('/')  # редиректим пользователя на главную страницу


def sign_out(request):
    logout(request)
    return render(request, 'account/logout.html', context={
            'page_name': 'Выход',
            'page_app': 'account',
            'page_view': 'sign_out'
        })


def ajax_reg(request):
    response = dict()
    login_y = request.GET.get('login') # GET - константа, которая определяет тип запроса
    try:
        User.objects.get(username=login_y)
        response['message'] = 'Логин занят'
    except User.DoesNotExist:
        response['message'] = 'Ок'
    return JsonResponse(response)