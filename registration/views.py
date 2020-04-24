from django.shortcuts import render



def index(request):
    title = 'Index'
    return render(request, 'registration/index.html', {'title': title})

def register(request):
    title = 'Sign up'
    return render(request, 'registration/register.html', {'title': title})



def login(request):
    title = 'Sign in'
    context = {'title': title}
    return render(request, 'registration/login.html', context)
