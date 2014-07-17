from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'bookshelf.views.home_page',
                           name='home'),
                       url(r'^list-books/$', 'bookshelf.views.list_books',
                           name='list_books'),
                       url(r'^list-authors/$', 'bookshelf.views.list_authors',
                           name='list_authors'),
                       url(r'^list-genres/$', 'bookshelf.views.list_genres',
                           name='list_genres'),
                       url(r'^get/$', 'bookshelf.views.get_book',
                           name='get_book'),
                       url(r'^add/$', 'bookshelf.views.add_book_form',
                           name='add_book_form'),
                       url(r'^add-book/$', 'bookshelf.views.add_book',
                           name='add_book'),
                       url(r'^edit-author/(?P<author_id>\d+)/$',
                           'bookshelf.views.edit_author',
                           name='edit_author'),
                       url(r'^save-edit-author/(?P<author_id>\d+)/$',
                           'bookshelf.views.save_edit_author',
                           name='save_edit_author'),
                       url(r'^bookshelf/(?P<book_id>\d+)/$',
                           'bookshelf.views.see_book', name='see_book'),
                       url(r'^bookshelf/authors/(?P<author_id>\d+)/$',
                           'bookshelf.views.see_author', name='see_author'),
                       url(r'^bookshelf/genres/(?P<genre_id>\d+)/$',
                           'bookshelf.views.see_genre', name='see_genre'),
                       # url(r'bookshelf/$', include('bookshelf.urls',
                       #                             namespace='bookshelf')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^forums/admin/', include(admin.site.urls)),
                       url(r'^forums/$', 'forums.views.home_forums',
                           name='forums-home'),
                       url(r'^forums/view-forum/(?P<forum_id>\d+)/$',
                           'forums.views.view_forum', name='view_forum'),
                       url(r'^forums/(?P<forum_id>\d+)/add-topic/$',
                           'forums.views.add_topic', name='add_topic'),
                       url(r'^forums/add-new-topic/(?P<forum_id>\d+)/$',
                           'forums.views.new_topic',
                           name='new_topic'),
                       url(r'^forums/view-topic/(?P<topic_id>\d+)/$',
                           'forums.views.view_topic', name='view_topic'),
                       url(r'^forums/(?P<topic_id>\d+)/reply/$',
                           'forums.views.reply', name='reply'),
                       url(r'^forums/post-reply/(?P<topic_id>\d+)/$',
                           'forums.views.post_reply', name='post_reply'),
                       url(r'^about-us/$', 'bookshelf.views.about',
                           name='about')
                       # url(r'^forums/$', include('forums.urls',
                       #     namespace='forums'))
                       )
