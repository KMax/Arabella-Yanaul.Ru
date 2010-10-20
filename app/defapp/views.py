# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

def start_page(request):
    return render_to_response('index.html',locals())

def about_us(request):
    return render_to_response('about.html', locals())

def services(request):
    return render_to_response('services.html', locals())

def prices(request):
    return render_to_response('prices.html', locals())

def contacts(request):
    return render_to_response('contacts.html', locals())