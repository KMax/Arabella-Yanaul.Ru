# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.fields import DateTimeField

class Answer(models.Model):
    text = models.TextField(verbose_name='Ответ')
    owner = models.CharField(verbose_name='Пользователь', max_length=100)
    review = models.OneToOneField('Review', related_name='review', verbose_name='Вопрос')

    def __unicode__(self):
        return u"%s - %s %s"%(
            unicode(self.owner),
            unicode(self.question.owner),
            unicode(self.question.date),
        )

class Review(models.Model):
    TYPES = (
        ('Q', u'Вопрос'),
        ('C', u'Жалоба'),
        ('S', u'Предложение'),
    )
    text = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(verbose_name='Дата и время публикации')
    owner = models.CharField(verbose_name='Имя пользователя', max_length=100)
    answer = models.OneToOneField(Answer, related_name='answer', verbose_name='Ответ', null=True, blank=True)
    type = models.CharField(max_length=1, choices=TYPES, verbose_name='Тип')

    def __unicode__(self):
        return u"%s %s %s %s" % (
            unicode(self.date.isoformat()),
            self.get_type_display(),
            self.owner,
            self.text,
        )