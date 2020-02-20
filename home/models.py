from django.db import models
from django.contrib.auth.models import User


class Gamer(models.Model):
    name = models.CharField(max_length=80, default='')
    
    def __str__(self):
        return self.name


class Score(models.Model):
    user = models.ForeignKey(Gamer, null=True, blank=True,
        on_delete=models.SET_NULL)
    score = models.IntegerField()
    
    def __str__(self):
        return self.user.name
