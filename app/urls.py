from django.conf.urls.defaults import patterns, include
from defapp.views import index_page
from app import settings
from django.conf.urls.defaults import handler404
from django.views.defaults import page_not_found
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', index_page),
    (r'^news/', include('app.news.urls')),
    (r'^gallery/', include('app.gallery.urls')),
    (r'^admin/',include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    (handler404, page_not_found),
#    (r'^about/$', about_us),
#    (r'^qa/', include('qa.urls')),
#    (r'^gallery/$', start_page),
#    (r'^login/$', login_page),
#    (r'^logout/$', logout_page),
#    (r'^admin/', include('adminpanel.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': '/media/Misc/Programming/Arabella-Yanaul.Ru/app/media'}),
    )
