# -*- coding: utf-8 -*-

from django.db import models
from sorl.thumbnail import ImageField

class Photo(models.Model):
    name = models.CharField(max_length=1000, verbose_name="название")
    pub_date = models.DateField(verbose_name="дата публикации")
    image = ImageField(upload_to="gallery/images")

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        db_table = "gallery"
        verbose_name="фото"
        verbose_name_plural = "фото"

class Album(models.Model):
    name = models.CharField(max_length=255, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    pub_date = models.DateField(verbose_name="дата публикации")
    cover = models.ForeignKey(Photo, verbose_name="обложка")

    class Meta:
        db_table = "album"
        verbose_name = "альбом"
        verbose_name_plural = "альбомы"
