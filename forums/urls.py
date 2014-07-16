from django.conf.urls import patterns, url, include
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'forums.views.home', name='home'),
                       url(r'^view-forum/(?P<forum_id>\d+)/$',
                           'forums.views.view_forum', name='view_forum'),
                       url(r'^admin/', include(admin.site.urls)),
                       # url(r'^add-forum/$', 'forums.views.add_forum',
                       #     name='add_forum'),
                       )
