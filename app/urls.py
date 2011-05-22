from django.conf.urls.defaults import patterns
from defapp.views import preview_page
from app import settings

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
