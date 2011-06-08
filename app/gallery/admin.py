# -*- coding: utf-8 -*-

from django.contrib import admin
from gallery.models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_date', 'name', 'image')

admin.site.register(Photo, PhotoAdmin)