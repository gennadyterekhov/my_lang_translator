from django.db import models
from user.models import User
from phonology.models import Consonant, Vowel
class Conlang(models.Model):
    original_name = models.CharField(max_length=80)
    english_name = models.CharField(max_length=80)
    description = models.TextField(max_length=999999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consonants = models.ManyToManyField(Consonant)
    vowels = models.ManyToManyField(Vowel)
    
    
    def __str__(self):
        return self.english_name
    
    
    def __unicode__(self):
        return self.english_name

