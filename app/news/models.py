# -*- coding: utf-8 -*-

from django.db import models

class News(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=255)
    text = models.TextField()

    class Meta:
        db_table = 'news'