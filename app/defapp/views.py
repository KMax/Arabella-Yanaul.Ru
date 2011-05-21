# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from news.models import News
from services.models import ServiceSection

def start_page(request):
    news_list = News.objects.order_by('-date')
    return render_to_response('index.html',locals())

def about_us(request):
    return render_to_response('about.html', locals())

def prices(request):
    return render_to_response('prices.html', locals())

def contacts(request):
    return render_to_response('contacts.html', locals())

def login_page(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request,user)
        return HttpResponseRedirect("/")
    else:
        return render_to_response('login.html',locals())

def logout_page(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def preview_page(request):
    return render_to_response('preview.html',locals())