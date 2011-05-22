# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

def start_page(request):
    return  render_to_response('news.html', locals())