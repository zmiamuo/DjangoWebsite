from django.contrib.auth.models import AbstractUser
from django.db import models
from django_quill.fields import QuillField

# Create your models here.

class User(AbstractUser):
    pass

class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=56)
    title = models.CharField(max_length=56)
    body = QuillField(blank=True, null=True)    
    cue = models.CharField(max_length=500, null=True)
    summary = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.title 

class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    esubject = models.CharField(max_length=56)
    date = models.DateField()
    details = models.CharField(max_length=56, null=True)
    theme = models.CharField(max_length=24, null=True)

    def __str__(self):
        return self.esubject 
 