from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from user.models import User
from conlang_creator.models import Conlang

def index(request):
    conlangs = Conlang.objects.all()
    try:
        user_id = request.session['user_id']
    except KeyError:
        # print(user_id)
        title = 'Conlang creator'
        user = {}
        conlangs = []
        context = {'title': title, 'user': user, 'conlangs': conlangs}
        return render(request, 'my_lang/index.html', context)
    


    title = 'Conlang creator'
    user = {}
    conlangs = []
    context = {'title': title, 'user': user, 'conlangs': conlangs}
    return render(request, 'my_lang/index.html', context)

    # user = get_object_or_404(User, pk=user_id)
    # title = 'Conlang creator'
    # context = {'title': title, 'user': user, 'conlangs': conlangs}
    # return render(request, 'my_lang/index.html', context)