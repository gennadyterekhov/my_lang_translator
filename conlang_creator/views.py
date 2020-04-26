from django.shortcuts import render, get_object_or_404
from user.models import User

from conlang_creator.models import Conlang


def create(request):
    title = 'Conlang creator'
    template = 'conlang_creator/create.html'

    user = get_object_or_404(User, pk=request.session['user_id'])
    context = {'title': title, 'user': user}
    return render(request, template, context)

def create_check(request):
    title = 'Conlang profile'

    user = get_object_or_404(User, pk=request.session['user_id'])

    original_name = request.POST.get('original_name', False)
    english_name = request.POST.get('english_name', False)
    description = request.POST.get('description', False)
    creator_user_id = request.POST.get('user_id', False)

    conlang = Conlang(original_name=original_name, english_name=english_name, description=description, user_id=creator_user_id)
    conlang.save()

    template = 'conlang_creator/profile.html'
    context = {'title': title, 'user': user, 'conlang': conlang}
    return render(request, template, context)


def profile(request, conlang_id):
    user = get_object_or_404(User, pk=request.session['user_id'])
    conlang = get_object_or_404(Conlang, pk=conlang_id)
    title = 'Conlang profile'
    template = 'conlang_creator/profile.html'
    context = {'title': title, 'user': user, 'conlang': conlang}
    return render(request, template, context)

# <a href="{% url 'conlang_creator:profile' conlang.id %}">{{ conlang.english_name }}</a>
def conlang_list(request):
    user = get_object_or_404(User, pk=request.session['user_id'])
    all_conlangs = Conlang.objects.all()
    conlangs = []
    for conlang in all_conlangs:
        temp_user = get_object_or_404(User, pk=conlang.user_id)
        temp = {
            'original_name': conlang.original_name,
            'english_name': conlang.english_name,
            'description': conlang.description,
            'user_name': temp_user.name,
            'user_email': temp_user.email,
            }
        conlangs.append(temp)
    title = 'Conlang list'
    template = 'conlang_creator/list.html'
    context = {'title': title, 'user': user, 'conlangs': conlangs}
    return render(request, template, context)
