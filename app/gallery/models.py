# -*- coding: utf-8 -*-

from django.db import models

class Photo(models.Model):
    name = models.CharField(max_length=1000, verbose_name="название")
    pub_date = models.DateField(verbose_name="дата публикации")
    image = models.ImageField(upload_to="gallery/images")

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        db_table = "gallery"
        verbose_name="фото"
        verbose_name_plural = "фото"


