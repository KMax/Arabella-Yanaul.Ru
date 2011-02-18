# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns

urlpatterns = patterns('adminpanel.views',
        (r'^$','admin_page'),
        (r'^qa/$','qa_page'),
        (r'^qa/show/\d*/$','qa_get_review'),
        (r'^services','admin_page'),
        (r'^gallery','admin_page'),
)