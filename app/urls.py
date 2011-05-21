from django.conf.urls.defaults import patterns, include
from defapp.views import start_page
from defapp.views import about_us
from defapp.views import login_page
from defapp.views import logout_page
from defapp.views import preview_page
from django.contrib import admin
from app import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', preview_page),
#    (r'^services/', include('services.urls')),
#    (r'^about/$', about_us),
#    (r'^qa/', include('qa.urls')),
#    (r'^gallery/$', start_page),
#    (r'^login/$', login_page),
#    (r'^logout/$', logout_page),
#    (r'^admin/', include('adminpanel.urls')),
#    (r'^superadmin/',include(admin.site.urls)),
#    (r'^admin_tools/', include('admin_tools.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': '/media/Misc/Programming/Arabella-Yanaul.Ru/app/media'}),
    )
