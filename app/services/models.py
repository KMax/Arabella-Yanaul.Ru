# -*- coding: utf-8 -*-

from django.db import models
import json

class ServiceSection(models.Model):
    title = models.CharField(max_length=255, verbose_name='Раздел')

    def get_services(self):
        return Service.objects.filter(section=self)

    def __unicode__(self):
        return "%s" % self.title

    class Meta:
        db_table = 'service_section'

class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание услуги')
    section = models.ForeignKey(ServiceSection, verbose_name='Раздел')

    class Meta:
        db_table = 'service'

class Price(models.Model):
    service = models.ForeignKey(Service, related_name='prices')
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

class PriceJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,Price):
            return {
                'title': o.title,
                'price': o.price,
            }
        return json.JSONEncoder().default(o)

class ServiceJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,Service):
            return {
                'title': o.title,
                'description': o.description,
                'section': o.section.title,
                'prices': json.loads(
                    PriceJSONEncoder().encode(list(o.prices.all())))
                }
        return json.JSONEncoder().default(o)