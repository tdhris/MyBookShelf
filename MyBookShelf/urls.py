from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'bookshelf.views.home_page', name='home'),
                       url(r'^get/$', 'bookshelf.views.get_book', name='get_book'),
                       url(r'^bookshelf/(?P<book_id>\d+)/$', 'bookshelf.views.see_book', name='see_book'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
