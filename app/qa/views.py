# -*- coding: utf-8 -*-
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render_to_response
from qa.models import Review

def qa_main_page(request):
    question_list=Review.objects.all()
    return render_to_response('qa.html',locals())

def qa_show_questions(request):
    question_list=Review.objects.filter(type='Q')
    return render_to_response('qa.html',locals())

def qa_show_suggestions(request):
    question_list=Review.objects.filter(type='S')
    return render_to_response('qa.html',locals())

def qa_show_complaints(request):
    question_list=Review.objects.filter(type='C')
    return render_to_response('qa.html',locals())

def qa_add_question(request):
    if (request.method == 'POST') & (request.is_ajax()):
        q = Review()
        q.text = request.POST.get("review")
        q.owner = request.POST.get("name")
        q.date = datetime.now()
        q.type = 'Q'
        q.save()
        return HttpResponse("All okey!")
    else:
        return HttpResponse("Request not support!")