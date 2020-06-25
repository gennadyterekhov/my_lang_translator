from django.db import models
from user.models import User
from phonology.models import Consonant, Vowel
class Conlang(models.Model):
    original_name = models.CharField(max_length=80)
    english_name = models.CharField(max_length=80)
    description = models.TextField(max_length=999999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # так было на старой БД
    # consonants = models.ManyToManyField(Consonant)
    # vowels = models.ManyToManyField(Vowel)
    consonants = models.CharField(max_length=300, default='p t k')
    vowels = models.CharField(max_length=200, default='a i u')
    syllable_structure = models.CharField(max_length=10)
    word_structure = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.english_name
    
    
    def __unicode__(self):
        return self.english_name

