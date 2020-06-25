from django.shortcuts import render, get_object_or_404
from user.models import User

# Create your views here.
def profile(request, user_id):
    title = 'Profile'
    template = 'user/profile.html'
    user = get_object_or_404(User, pk=user_id)
    conlangs = user.conlang_set.all()
    context = {'title': title, 'user': user, 'conlangs': conlangs}
    return render(request, template, context)


def user_list(request):
    title = 'User list'
    users = User.objects.all()
    user = get_object_or_404(User, pk=request.session['user_id'])
    template = 'user/list.html'
    context = {'title': title, 'user': user, 'users': users}
    return render(request, template, context)