# -*- coding: utf-8 -*-

from django.contrib import admin
from qa.models import Review, Answer

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('date','type','text','owner_name',)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('review','text',)

admin.site.register(Review, ReviewAdmin)
admin.site.register(Answer, AnswerAdmin)
  