from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("<h1>hello</h1><br><a href='translate/'>translator</a>")
    return render(request, 'my_lang/index.html', {})