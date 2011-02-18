# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from qa.models import Review

def admin_page(request):
    return render_to_response('adminpanel/base.html',locals())

def qa_page(request):
    action="view.all"
    question_list=Review.objects.order_by('id')
    return render_to_response('adminpanel/qa.html',locals())

def qa_view_selected(request):
    wert="Привет!"
    return render_to_response('adminpanel/qa.html',locals())