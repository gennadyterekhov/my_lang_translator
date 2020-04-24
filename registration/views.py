from django.shortcuts import render
from .models import User


def index(request):
    title = 'Index'
    return render(request, 'registration/index.html', {'title': title})


def register(request):
    title = 'Sign up'
    return render(request, 'registration/register.html', {'title': title})


def login_check(request):
    title = 'Amʔanavio'

    email = request._get_post()['email']
    password = request._get_post()['password']

    # ищем в бд
    passed_users = User.objects.filter(email=email, password=password)
    if passed_users:
        return render(request, 'my_lang/index.html', {'title': title, 'user_name': passed_users[0].name})
    else:
        title = 'Sign in'
        error_message = 'User not found'
        return render(request, 'registration/login.html', {'title': title, 'error_message': error_message})

    return render(request, 'my_lang/index.html', {'title': title})


def is_valid_email(email):
    return True


def register_check(request):
    title = 'Amʔanavio'

    # print(request._get_post()['login'])

    email = request._get_post()['email']
    name = request._get_post()['name']
    password = request._get_post()['password']

    if is_valid_email(email):
        registered_user = User(email=email, name=name, password=password)
        registered_user.save()
        return render(request, 'my_lang/index.html', {'title': title, 'user_name': registered_user.name})
    else:
        title = 'Sign up'
        error_message = 'Invalid email'
        return render(request, 'registration/register.html', {'title': title, 'error_message': error_message})

    return render(request, 'my_lang/index.html', {'title': title})


def login(request):
    title = 'Sign in'
    context = {'title': title}
    return render(request, 'registration/login.html', context)
