from django.shortcuts import render, get_object_or_404
from user.models import User
from django.contrib.auth import hashers


def login(request):
    title = 'Sign in'
    context = {'title': title}
    template = 'registration/login.html'
    return render(request, template, context)


def register(request):
    title = 'Sign up'
    template = 'registration/register.html'
    context = {'title': title}
    return render(request, template, context)


def login_check(request):
    title = 'Amʔanavio'

    email = request._get_post()['email']
    password = request._get_post()['password']

    passed_users = User.objects.filter(email=email)
    user = passed_users[0]
    if user:
        if  hashers.check_password(password, user.password):
            request.session['user_id'] = user.id
            request.session.save()
            return render(request, 'my_lang/index.html', {'title': title, 'user': user})
        else:
            title = 'Sign in'
            error_message = 'Wrong credentials'
            return render(request, 'registration/login.html', {'title': title, 'error_message': error_message})
    else:
        title = 'Sign in'
        error_message = 'User not found'
        return render(request, 'registration/login.html', {'title': title, 'error_message': error_message})


def register_check(request):

    email = request._get_post()['email']
    name = request._get_post()['name']
    password = request._get_post()['password'] # same as request.POST['password']

    hashed_password = hashers.make_password(password)
    user = User(email=email, name=name, password=hashed_password)
    user.save()
    request.session['user_id'] = user.id
    request.session.save()

    title = 'Amʔanavio'
    template = 'my_lang/index.html'
    context = {'title': title, 'user': user}
    return render(request, template, context)


def logout(request):
    # request.session.flush()
    request.session['user_id'] = None
    request.session.save()

    title = 'Amʔanavio'
    template = 'my_lang/index.html'
    context = {'title': title}
    return render(request, template, context)