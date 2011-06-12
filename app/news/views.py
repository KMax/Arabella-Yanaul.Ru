# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from news.models import News

news_per_page = 4

def start_page(request):
    return get_page(1)

def get_news(request, id='1'):
    news = News.objects.get(id=id)
    return render_to_response('news.html',locals())

def get_page(request, page_id='1'):
    page_id = int(page_id)
    if page_id > 1:
        pred_page_id = page_id - 1
    if News.objects.count() > news_per_page*page_id:
        next_page_id = page_id + 1
    news_list = News.objects.\
                order_by('-date')[news_per_page*(page_id-1):news_per_page*page_id]
    return render_to_response('news_list.html', locals())