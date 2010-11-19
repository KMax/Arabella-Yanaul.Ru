'''
Created on 23.10.2010

@author: Maxim Kolchin
'''

from django.db import models
from app.defapp.models import User

class Question(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User)
    answer = models.OneToOneField('Answer', related_name='Answer.question')
    
class Answer(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User)
    question = models.OneToOneField(Question, related_name='Question.answer')