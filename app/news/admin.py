# -*- coding: utf-8 -*-

from django.contrib import admin
from news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date','title')
    list_filter = ['date']
    search_fields = ['title', 'text']
    date_hierarchy = 'date'
    list_per_page = 10

admin.site.register(News, NewsAdmin)