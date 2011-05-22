from django.conf.urls.defaults import patterns, include
from defapp.views import index_page
from app import settings

urlpatterns = patterns('',
    (r'^$', index_page),
    (r'^news/', include('app.news.urls')),
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
