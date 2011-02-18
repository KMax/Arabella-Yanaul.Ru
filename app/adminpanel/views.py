# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from qa.models import Review, ReviewJSONEncoder

def admin_page(request):
    return render_to_response('adminpanel/base.html',locals())

def qa_page(request):
    action="view.all"
    review_list=Review.objects.order_by('id')
    return render_to_response('adminpanel/qa.html',locals())

def qa_get_review(request):
    if(request.method == 'POST') & (request.is_ajax()):
        review = Review.objects.get(id=request.POST.get("id"))
        return HttpResponse(content=ReviewJSONEncoder().encode(review),mimetype="application/json")
    else:
        return HttpResponse("Error! This request isn't ajax!")