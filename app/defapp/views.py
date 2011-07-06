# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from news.models import News

def index_page(request):
    return render_to_response('index.html',locals())