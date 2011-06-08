# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from news.models import News

class LatesNewsFeed(Feed):
    title = "Новости и акции салона красоты 'Шарм'"
    link = "/news/"
    description = "Последнии новости с сайта салона красоты 'Шарм'"

    def items(self):
        return News.objects.order_by('-date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return "/news/"