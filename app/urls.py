from django.conf.urls.defaults import patterns, include
import adminpanel
from defapp.views import start_page
from defapp.views import services
from defapp.views import about_us
from defapp.views import login_page
from defapp.views import logout_page
from django.contrib import admin
from adminpanel.views import admin_page
from app import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', start_page),
    (r'^services/$', services),
    (r'^about/$', about_us),
    (r'^qa/', include('qa.urls')),
    (r'^gallery/$', start_page),
    (r'^login/$', login_page),
    (r'^logout/$', logout_page),
    (r'^admin/', include('adminpanel.urls')),
    (r'^superadmin/',include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': '/media/Misc/Programming/Arabella-Yanaul.Ru/app/media'}),
    )
