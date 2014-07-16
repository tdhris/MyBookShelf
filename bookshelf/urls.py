from django.conf.urls import patterns, url

urlpatterns = patterns('',
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
                       url(r'^bookshelf/(?P<book_id>\d+)/$',
                           'bookshelf.views.see_book', name='see_book'),
                       )
