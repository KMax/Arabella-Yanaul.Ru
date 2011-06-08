# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns
from news.feed import LatesNewsFeed

urlpatterns = patterns('news.views',
    (r'^$', 'start_page'),
    (r'^feed/$', LatesNewsFeed())
)