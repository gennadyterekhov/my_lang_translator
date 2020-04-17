from django.shortcuts import render
from django.http import HttpResponse

from .my_lang_translator import main

def translate(text):
    return main.main(text)


def translate_esperanto(text):
    return main.translate_esperanto(text)


def index(request):
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
            result = translate(text_to_translate)
    return render(request, 'translator/index.html', {'text_to_translate': text_to_translate, 'result': result, 'esperanto': esperanto})


def result(request):
    t = request.GET.get('text', '')
    # te = request.GET['text']
    # print(te)
    result = 'text that you typed: {}'.format(t)
    return render(request, 'translator/index.html', {'text': t, 'result': result})