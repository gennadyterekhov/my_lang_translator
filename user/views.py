from django.shortcuts import render, get_object_or_404
from registration.models import User

# Create your views here.
def profile(request, user_id):
    title = 'Profile'
    template = 'user/profile.html'
    # user = User.objects.filter(email=request.session['email'])[0]
    # user = User.objects.filter(id=user_id)[0]
    user = get_object_or_404(User, pk=user_id)
    context = {'title': title, 'user': user}
    return render(request, template, context)


def user_list(request):
    title = 'User list'
    users = User.objects.all()
    # user = User.objects.filter(email=request.session['email'])[0]
    user = get_object_or_404(User, email=request.session['email'])
    template = 'user/list.html'
    context = {'title': title, 'user': user, 'users': users}
    return render(request, template, context)