from django.db import models
from user.models import User

class Conlang(models.Model):
    original_name = models.CharField(max_length=80)
    english_name = models.CharField(max_length=80)
    description = models.TextField(max_length=999999)
    # user_id = models.CharField(max_length=80)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # def __init__(self, original_name, english_name, description):
    #     self.original_name = original_name
    #     self.english_name = english_name
    #     self.description = description
    
    
    def __str__(self):
        return self.english_name
    
    
    def __unicode__(self):
        return self.english_name
