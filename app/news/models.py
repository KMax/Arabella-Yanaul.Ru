# -*- coding: utf-8 -*-

from django.db import models

class News(models.Model):
    date = models.DateField(verbose_name="Дата публикации")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст новости")

    def intro(self):
        text = unicode(News.objects.get(id=self.id).text).\
        partition("<!--pagebreak-->")
        return text[0]

    def is_short_news(self):
        text = unicode(News.objects.get(id=self.id).text).\
        partition("<!--pagebreak-->")
        if text[1]: 
            return False
        else:
            return True

    class Meta:
        db_table = 'news'
        verbose_name = 'новость'
        verbose_name_plural = 'новости'