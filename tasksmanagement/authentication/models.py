from django.db import models
from django.forms import NullBooleanField



# Create your models here.
class Task(models.Model):
    
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=250)
    status =  models.BooleanField(default=False)
    deleteall =  models.BooleanField(default=False)