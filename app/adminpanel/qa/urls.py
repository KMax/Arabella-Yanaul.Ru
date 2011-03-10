# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns
import adminpanel

urlpatterns = patterns('adminpanel.qa.views',
        (r'^$','main'),
        (r'show/all','get_all_review'),
        (r'show/unanswered','get_unanswered_review'),
        (r'show/complaint','get_complaint_review'),
        (r'show/supply','get_supply_review'),
        (r'show/question','get_question_review'),
        (r'show','get_review'),
        (r'save/answer','save_answer'),
        (r'delete','delete_review'),
)