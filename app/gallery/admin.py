# -*- coding: utf-8 -*-

from django.contrib import admin
from gallery.models import Photo, Album
from sorl.thumbnail.admin import AdminImageMixin

class PhotoAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('id', 'pub_date', 'name', 'image')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id','pub_date', 'name')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)