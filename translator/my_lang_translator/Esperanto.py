from . import esperanto_config
from . import Language

class Esperanto(Language.Language):
    def __init__(self):
        pass
    

    def get_morphemes_from_eo_word(self, word):
        
        return word


    def get_corresponding_morpheme(self, morpheme):
        return morpheme


    def translate_word(self, word):
        word = word.strip()
        morphology = self.get_morphemes_from_eo_word(word)
        res = '-'.join(list(map(self.get_corresponding_morpheme, morphology)))
        return res 


    def translate_from_eo(self, text):
        res = ' '.join(list(map(self.translate_word, text.split(' '))))
        return res


class EsperantoWord(Language.Word):
    def __init__(self, spelling):
        self.spelling = self.remove_punctuation(spelling)
        self.ending = self.get_ending()
        self.root = self.get_root()
        self.number_of_syllables = self.get_number_of_syllables()
    

    def get_number_of_syllables(self):
        vowels = 'a i u e o'.split()
        count = 0
        for char in self.spelling:
            if char in vowels:
                count += 1
        return count


    def get_root(self):
        return self.spelling[:self.spelling.index(self.ending)]


    def get_ending(self):
        ending = ''
        if self.spelling[-1] in esperanto_config.one_letter_endings:
            return self.spelling[-1]
        elif self.spelling[-2:] in esperanto_config.two_letter_endings:
            return self.spelling[-2:]
        elif self.spelling[-3:] in esperanto_config.three_letter_endings:
            return self.spelling[-3:]
        return ending


    def get_morphemes(self):
        return [self.root, self.ending]
    

    def remove_punctuation(self, text):
        punctuation = '. / , ; : \' \\ \" [ ] { } ( ) * ! & ? < > @ # $ % ^ _ - = + ` ~'.split(' ')
        revised_text = ''
        for char in text:
            if char not in punctuation:
                revised_text += char
                
        return revised_text