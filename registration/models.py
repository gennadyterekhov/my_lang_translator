from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=80)
    name = models.CharField(max_length=80)
    password = models.CharField(max_length=256)
    conlangs = []
    
    
    def __str__(self):
        return self.email


class Conlang(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
