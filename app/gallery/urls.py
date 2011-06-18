# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns

urlpatterns = patterns('gallery.views',
    (r'^$', 'get_images'),
    (r'photo/[-10-9]*$','json_get_photo'),
)