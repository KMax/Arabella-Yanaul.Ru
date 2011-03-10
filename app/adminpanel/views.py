# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

def admin_page(request):
    return render_to_response('adminpanel/base.html',locals())