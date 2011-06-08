# -*- coding: utf-8 -*-

from django.contrib import admin
from news.models import News
from django.db import models
from tinymce.widgets import TinyMCE

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date','title')
    list_filter = ['date']
    search_fields = ['title', 'text']
    date_hierarchy = 'date'
    list_per_page = 10
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 100, 'rows': 30})}
    }

admin.site.register(News, NewsAdmin)