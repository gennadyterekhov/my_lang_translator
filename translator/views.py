from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .my_lang_translator import main
from . import translate
from . import config

from user.models import User

def translate_esperanto(text):
    translator = translate.Translator(config.API_KEY)
    return translator.yandex_translate('eo', text)


def translate_to_conlang(text):
    translator = translate.Translator(config.API_KEY)
    return translator.translate_from_eo_to_conlang(text)


def index(request):
    title = 'Translate'
    text_to_translate = request.GET.get('text', '')
    if text_to_translate == '':
        esperanto = ''
        result = ''
    else:
        esperanto = translate_esperanto(text_to_translate)
        if esperanto == text_to_translate:
            # english and esperanto is similiar
            result = esperanto
        else:
            result = translate_to_conlang(esperanto)

    # user = User.objects.filter(pk=request.session['user_id'])[0]
    user = get_object_or_404(User, pk=request.session['user_id'])
    context = {'title': title, 'user': user, 'text_to_translate': text_to_translate, 'result': result, 'esperanto': esperanto}
    return render(request, 'translator/index.html', context)


def result(request):
    title = 'Translate'
    t = request.GET.get('text', '')
    # te = request.GET['text']
    # print(te)
    result = 'text that you typed: {}'.format(t)
    
    # user = User.objects.filter(pk=request.session['user_id'])[0]
    user = get_object_or_404(User, pk=request.session['user_id'])
    context = {'title': title, 'user': user, 'text': t, 'result': result}
    return render(request, 'translator/index.html', context)