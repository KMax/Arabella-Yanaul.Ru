# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from services.models import ServiceSection, Service, ServiceJSONEncoder

def get_main_page(request):
    section_list = ServiceSection.objects.all()
    return render_to_response('services.html', locals())

def json_get_service(request, id=1):
    try:
        serv = Service.objects.get(id=id)
    except Service.DoesNotExist:
        return HttpResponse(status=404)
    return HttpResponse(content=ServiceJSONEncoder().encode(serv),
                        mimetype="application/json; charset=utf-8")
