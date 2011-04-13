# -*- coding: utf-8 -*-

from django.contrib import admin
from news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')

admin.site.register(News, NewsAdmin)