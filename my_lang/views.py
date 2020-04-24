from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from registration.models import User

def index(request):
    # title = 'Amʔanavio'
    title = 'Conlang creator'
    # user = User.objects.filter(email=request.session['email'])[0]
    user = get_object_or_404(User, email=request.session['email'])
    context = {'title': title, 'user': user}
    return render(request, 'my_lang/index.html', context)