class Language:
    def __init__(self, name, phonology):
        self.name = name
        self.phonology = phonology
        # self.consonants = consonants
        # self.vowels = vowels


    def set_phonology(self, phonology):
        self.phonology = phonology


    def generate_word(self, l):
        # generate new word of len l
        word = ''
        for c in self.phonology.consonants:
            for v in self.phonology.vowels:
                word += c + v
        return word


class Phonology:
    def __init__(self, consonants, vowels):
        self.consonants = consonants
        self.vowels = vowels


class Word:
    def __init__(self, spelling):
        self.spelling = self.remove_punctuation(spelling)
        self.number_of_syllables = self.get_number_of_syllables()
    

    def get_number_of_syllables(self):
        vowels = 'a i u e o å ū'.split()
        count = 0
        for char in self.spelling:
            if char in vowels:
                count += 1
        return count
    

    def remove_punctuation(self, text):
        punctuation = '. / , ; : \' \\ \" [ ] { } ( ) * ! & ? < > @ # $ % ^ _ - = + ` ~'.split(' ')
        revised_text = ''
        for char in text:
            if char not in punctuation:
                revised_text += char
                
        return revised_text
