# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from news.models import News

def start_page(request):
    news_list = News.objects.all()
    return render_to_response('news.html', locals())