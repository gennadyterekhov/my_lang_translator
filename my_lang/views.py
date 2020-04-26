from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from user.models import User
from conlang_creator.models import Conlang

def index(request):
    conlangs = Conlang.objects.all()
    user = get_object_or_404(User, pk=request.session['user_id'])
    title = 'Conlang creator'
    context = {'title': title, 'user': user, 'conlangs': conlangs}
    return render(request, 'my_lang/index.html', context)