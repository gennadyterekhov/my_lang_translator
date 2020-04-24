from django.shortcuts import render, get_object_or_404
from .models import User
# from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth import hashers

def index(request):
    title = 'Index'
    # user = User.objects.filter(email=request.session['email'])[0]
    user = get_object_or_404(User, email=request.session['email'])
    context = {'title': title, 'user': user}
    return render(request, 'registration/index.html', context)


def register(request):
    title = 'Sign up'
    return render(request, 'registration/register.html', {'title': title})


def login_check(request):
    title = 'Amʔanavio'

    email = request._get_post()['email']
    password = request._get_post()['password']

    # ищем в бд
    passed_users = User.objects.filter(email=email)
    if passed_users[0]:
        valid_password = hashers.check_password(password, passed_users[0].password)
        if valid_password:
            request.session.__setitem__('email', passed_users[0].email)
            request.session.save()
            return render(request, 'my_lang/index.html', {'title': title, 'user_name': passed_users[0].name, 'user': passed_users[0]})
        else:
            title = 'Sign in'
            error_message = 'Wrong credentials'
            return render(request, 'registration/login.html', {'title': title, 'error_message': error_message})

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
    password = request._get_post()['password'] # same as request.POST['password']

    if is_valid_email(email):
        # hashed_password = PBKDF2PasswordHasher.make_password(password)
        hashed_password = hashers.make_password(password)
        registered_user = User(email=email, name=name, password=hashed_password)
        registered_user.save()
        request.session.__setitem__('email', email)
        request.session.save()
        return render(request, 'my_lang/index.html', {'title': title, 'user_name': registered_user.name, 'user': registered_user})
    else:
        title = 'Sign up'
        error_message = 'Invalid email'
        return render(request, 'registration/register.html', {'title': title, 'error_message': error_message})

    return render(request, 'my_lang/index.html', {'title': title})


def login(request):
    title = 'Sign in'
    context = {'title': title}
    return render(request, 'registration/login.html', context)


def logout(request):
    title = 'Amʔanavio'
    # request.session.flush()
    request.session['email'] = None
    request.session.save()
    return render(request, 'my_lang/index.html', {'title': title})