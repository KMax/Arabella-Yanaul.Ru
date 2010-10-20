from defapp.views import start_page
from defapp.views import services
from defapp.views import about_us
from defapp.views import prices
from defapp.views import contacts
from app import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', start_page),
    (r'^services/$', services),
    (r'^about/$', about_us),
    (r'^prices/$', prices),
    (r'^contacts/$', contacts),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': '/media/Misc/Programming/Source/Arabella/Arabella/media/'}),
    )
