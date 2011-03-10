# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include

urlpatterns = patterns('adminpanel.views',
        (r'^$','admin_page'),
        (r'^services','admin_page'),
        (r'^gallery','admin_page'),
        (r'qa',include('adminpanel.qa.urls')),
)