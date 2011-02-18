from django.conf.urls.defaults import patterns

urlpatterns = patterns('qa.views',
        (r'^$', 'qa_main_page'),
        (r'^questions/$', 'qa_show_questions'),
        (r'^suggestions/$', 'qa_show_suggestions'),
        (r'^complaints/$', 'qa_show_complaints'),
        (r'^add/$', 'qa_add_question'),
                       )