# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from gallery.models import Photo
from app.utils.response import JSONResponse

def start_page(request):
    photos = Photo.objects.order_by("-pub_date")[:2]
    current = photos[0]
    next = photos[1]
    return render_to_response("gallery.html",locals())

def json_get_photo(request):
    if request.method == "POST":
        id = int(request.POST["id"])
        photo_list = Photo.objects.order_by("-pub_date")
        if id > photo_list.count()-1:
            id = 0
        if id < 0:
            id = photo_list.count()-1
        photo = Photo.objects.order_by("-pub_date")[id]
        return JSONResponse({"id":id,"name":photo.name,"url":photo.image.url})