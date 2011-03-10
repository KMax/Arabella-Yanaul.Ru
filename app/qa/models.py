# -*- coding: utf-8 -*-
import json
from django.db import models
from django.db.models.fields import DateTimeField

class Answer(models.Model):
    text = models.TextField(verbose_name='Ответ')
    owner = models.CharField(verbose_name='Пользователь', max_length=100)
    review = models.OneToOneField('Review', related_name='review', verbose_name='Вопрос')

    def __unicode__(self):
        return u"%s - %s %s"%(
            unicode(self.owner),
            unicode(self.review.owner_name),
            unicode(self.review.date),
        )

class Review(models.Model):
    TYPES = (
        ('Q', u'Вопрос'),
        ('C', u'Жалоба'),
        ('S', u'Предложение'),
    )
    text = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(verbose_name='Дата и время публикации')
    owner_name = models.CharField(verbose_name='Имя пользователя', max_length=100)
    owner_email = models.EmailField(verbose_name='Емайл пользователя')
    answer = models.OneToOneField(Answer, related_name='answer', verbose_name='Ответ', null=True, blank=True)
    type = models.CharField(max_length=1, choices=TYPES, verbose_name='Тип')

    def __unicode__(self):
        return u"[%s] [%s] [%s] %s" % (
            unicode(self.date.isoformat()),
            self.get_type_display(),
            self.owner_name,
            self.text,
        )

    def has_answer(self):
        if self.answer is None:
            return False
        else:
            return  True

#Serialize Review object to JSON object
class ReviewJSONEncoder(json.JSONEncoder):
    def default(self,o):
        if isinstance(o,Review):
            return {'id':o.id, 'type':o.get_type_display(),
                    'date':o.date.isoformat(),
                    'owner_name':o.owner_name,
                    'text':o.text,
                    'owner_email': o.owner_email,
                    'has_answer': o.has_answer()
                }
        return json.JSONEncoder().default(o)