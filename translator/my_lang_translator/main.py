import requests
import json
import urllib

from . import config
from . import Conlang
from . import simple_replace

from . import lang_config

class Session:
    def __init__(self, key):
        self.key = key


    def wikipedia_query(self, text):
        text = urllib.parse.quote(text)
        query = '?action=query&list=search&srsearch={}&format=json'.format(text)
        res = requests.get('https://en.wikipedia.org/w/api.php' + query)
        return json.loads(res.text)


    def translate(self, origin_language, destination_language, text):
        text = urllib.parse.quote(text)
        query = '?lang={}-{}&text={}&key={}'.format(origin_language, destination_language, text, self.key)
        res = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate' + query)

        return json.loads(res.text)
    

    def print_first_snippet(self, response):
        print( response['query']['search'][0]['snippet'])



    def pretty_print_response(self, response):
        if isinstance(response, dict):
            for k, v in response.items():
                if isinstance(v, dict):
                    print('{')
                    self.pretty_print_response(v)
                    print('}')
                elif isinstance(v, list):
                    print('[')
                    for elem in v:
                        print(elem)
                    print(']')
                else:
                    print(k, ': ', v)
        else:
            print(response)


def translate_esperanto(text):
    s = Session(config.API_KEY)
    text_eo = s.translate('en', 'eo', text.lower())['text'][0]
    return text_eo


def main(text):
    s = Session(config.API_KEY)
    # text = input('enter text that you wish to translate:\n')
    # text = 'what is love'
    # text_eo = s.translate('en', 'eo', text.lower())['text'][0]
    response_translation = s.translate('en', 'eo', text.lower())
    print(response_translation)
    text_eo = response_translation['text'][0]


    my_phonology = Conlang.ConlangPhonology(lang_config.consonants, lang_config.vowels)
    my_lang = Conlang.Conlang('amʔanavi', my_phonology)
    text_my = my_lang.translate_from_eo(text_eo.lower())
    print(text_my)
    return text_my

    # можно так сделать: на каждое эо слово: если соответствие есть в словаре то вернуть его, если нет - генерировать новое
    # в словаре можно указывать только корни


    # response = s.wikipedia_query('Tamil script')
    # s.print_first_snippet(response)

    # res = simple_replace.replace_text(text_eo)
    # print(res)


# if __name__ == '__main__':
#     s = Session(config.API_KEY)
#     # text = input('enter text that you wish to translate:\n')
#     text = 'what is love'
#     text_eo = s.translate('en', 'eo', text.lower())['text'][0]
#     # text_eo = 'homaj rajtoj'

#     my_phonology = Conlang.ConlangPhonology(lang_config.consonants, lang_config.vowels)
#     my_lang = Conlang.Conlang('amʔanavi', my_phonology)
#     text_my = my_lang.translate_from_eo(text_eo.lower())
#     print(text_my)

#     # можно так сделать: на каждое эо слово: если соответствие есть в словаре то вернуть его, если нет - генерировать новое
#     # в словаре можно указывать только корни


#     # response = s.wikipedia_query('Tamil script')
#     # s.print_first_snippet(response)

#     # res = simple_replace.replace_text(text_eo)
#     # print(res)

