# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns

urlpatterns = patterns('news.views',
    (r'^$', 'start_page'),
)