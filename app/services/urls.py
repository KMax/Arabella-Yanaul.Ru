# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns

urlpatterns = patterns('services.views',
        (r'^$', 'get_main_page'),
        (r'(?P<id>\d+)$', 'json_get_service'),
)