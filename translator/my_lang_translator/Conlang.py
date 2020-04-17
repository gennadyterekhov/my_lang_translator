from . import Esperanto
from . import Language
from . import esperanto_config
from . import lang_config
import random

# import dictionary

class Conlang(Language.Language):
    def __init__(self, name, phonology):
        self.name = name
        self.phonology = phonology
        self.cvc_syllables = self.get_cvc_syllables()
        # self.all_possible_syllables
        super().__init__(name, phonology)


    def get_cvc_syllables(self):
        f = open('translator/my_lang_translator/syllables', 'r', encoding='utf8')
        contents = f.read()
        f.close()
        syllables = contents.split('\n')[:-1]
        return syllables


    def get_morphemes_from_eo_word(self, word):
        word_obj = Esperanto.EsperantoWord(word)
        return word_obj.get_morphemes()


    def get_corresponding_morpheme_old(self, morpheme):
        res = ''
        if morpheme in esperanto_config.morphemes:
            index = esperanto_config.morphemes.index(morpheme)
            res = lang_config.morphemes[index]
        return res


    def get_corresponding_morpheme(self, morpheme):
        res = ''
        d = open('translator/my_lang_translator/dictionary', 'r', encoding='utf8')
        for line in d.readlines():
            if morpheme == line.split(' ')[0]:
                res = line.split(' ')[1].strip()
        d.close()
        if res != '':
            return res
        
        new_word = self.generate_word(morpheme)
        d = open('translator/my_lang_translator/dictionary', 'a', encoding='utf8')
        d.write(morpheme + ' ' + new_word + '\n')
        d.close()
        return new_word


    def generate_word(self, morpheme):
        
        # generate new word with the same number of syllables as morpheme
        word_obj = Language.Word(morpheme)
        number_of_syllables = word_obj.number_of_syllables
        syllables = []
        for i in range(number_of_syllables):
            syllables.append(self.get_random_syllable())
        return ''.join(syllables)


    def get_random_syllable(self):
        number_of_syllables = len(self.cvc_syllables)
        random.seed()
        s = self.cvc_syllables[random.randint(0, number_of_syllables - 1)]
        return s
    
    
    def get_syllable(self):
        return 'a'



    def translate_word(self, word):
        word = word.strip()
        morphology = self.get_morphemes_from_eo_word(word)
        print(morphology)
        res = '-'.join(list(map(self.get_corresponding_morpheme, morphology)))
        return res 


    def translate_from_eo(self, text):
        res = ' '.join(list(map(self.translate_word, text.split(' '))))
        return res


class ConlangPhonology(Language.Phonology):
    def __init__(self, consonants, vowels):
        self.consonants = consonants
        self.vowels = vowels