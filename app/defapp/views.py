# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

def preview_page(request):
    return render_to_response('preview.html',locals())