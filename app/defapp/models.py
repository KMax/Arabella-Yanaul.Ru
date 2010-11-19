# -*- coding: utf-8 -*- 
from django.db import models

class User(models.Model):
    ROLE_CHOICES = (
                ('USER', 'Пользователь'),
                ('ADMIN', 'Администратор'),
                )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=5, choices=ROLE_CHOICES) #FIXME не прописывать жестко
    phone = models.CharField(max_length=20, blank=True, null=True) #FIXME
    email = models.EmailField()
    password = models.CharField(max_length=10, blank=True, null=True) #FIXME
    #image =  models.ImageField()
    