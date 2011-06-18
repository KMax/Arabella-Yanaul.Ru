# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from news.models import News

def index_page(request):
    return render_to_response('index.html',locals())

def pda_page(request):
    news_list = News.objects.order_by("-date")[:3]
    return render_to_response('pda.html', locals())