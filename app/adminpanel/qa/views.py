# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from qa.models import Review, ReviewJSONEncoder

def main(request):
    action="view.all"
    review_list=Review.objects.filter(answer__isnull=True)
    return render_to_response('adminpanel/qa.html',locals())

def get_review(request):
    if(request.method == 'POST') & (request.is_ajax()):
        review = Review.objects.get(id=request.POST.get("id"))
        return HttpResponse(content=ReviewJSONEncoder().encode(review),mimetype="application/json; charset=utf-8")
    else:
        return HttpResponse(status=400)

def get_all_review(request):
    if(request.method == 'POST') & (request.is_ajax()):
        review_list = Review.objects.order_by('date')
        return HttpResponse(content=json.dumps(list(review_list),cls=ReviewJSONEncoder),
                            mimetype="application/json; charset=utf-8")
    else:
        return HttpResponse(status=400)

def get_unanswered_review(request):
    if(request.method == 'POST') & (request.is_ajax()):
        review_list = Review.objects.filter(answer__isnull=True).order_by('date')
        return HttpResponse(content=json.dumps(list(review_list),cls=ReviewJSONEncoder),
                            mimetype="application/json; charset=utf-8")
    else:
        return HttpResponse(status=400)

def get_complaint_review(request):
    if(request.method == 'POST') & (request.is_ajax()):
        review_list = Review.objects.filter(type='C').order_by('date')
        return HttpResponse(content=json.dumps(list(review_list),cls=ReviewJSONEncoder),
                            mimetype="application/json; charset=utf-8")
    else:
        return HttpResponse(status=400)

def get_supply_review(request):
    if(request.method == 'POST') & (request.is_ajax()):
        review_list = Review.objects.filter(type='S').order_by('date')
        return HttpResponse(content=json.dumps(list(review_list),cls=ReviewJSONEncoder),
                            mimetype="application/json; charset=utf-8")
    else:
        return HttpResponse(status=400)

def get_question_review(request):
    if(request.method == 'POST') & (request.is_ajax()):
        review_list = Review.objects.filter(type='Q').order_by('date')
        return HttpResponse(content=json.dumps(list(review_list),cls=ReviewJSONEncoder),
                            mimetype="application/json; charset=utf-8")
    else:
        return HttpResponse(status=400)

def delete_review(request):
    if(request.method == 'POST') & (request.is_ajax()):
        review = Review.objects.get(id=request.POST.get("id"))
       #FIXME review.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)