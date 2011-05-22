# -*- coding: utf-8 -*-

from django.contrib import admin
from services.models import Service, ServiceSection, Price

class PriceInline(admin.TabularInline):
    model = Price
    fk_name = "service"

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','section', 'description')
    inlines = [
        PriceInline,
    ]

class ServiceSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceSection, ServiceSectionAdmin)
#admin.site.register(Price, PriceAdmin)