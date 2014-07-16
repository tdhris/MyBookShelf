from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import home_page
from .forms import SearchBookForm, AddBookForm
from .models import Book, Author, Genre

STATUS_CODE_OK = 200
STATUS_CODE_REDIRECT = 302


class HomePageTests(TestCase):
    def test_root_url_resolves_to_homepage(self):
        page = resolve('/')
        self.assertEqual(home_page, page.func)

    def test_home_page_view_renders_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'homepage.html')

    def test_homepage_has_book_search_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], SearchBookForm)


class GetBookTests(TestCase):
    def test_get_book_redirects_to_booknotfound_template_when_book_does_not_exist(self):
        response = self.client.post('/get/', data={'title': "Blah Blah Book"})
        self.assertTemplateUsed(response, 'book_not_found.html')

    def test_get_book_redirects_to_book_page_when_book_exists_in_database(self):
        jkrowling = Author.objects.create(name='J.K. Rowling')
        fantasy = Genre.objects.create(name='Fantasy')
        Book.objects.create(title='Harry Potter', author=jkrowling,
                            genre=fantasy, synopsis='Best Series Ever')
        response = self.client.post('/get/', data={'title': 'Harry Potter'}, follow=True)
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        self.assertTemplateUsed(response, 'book.html')


class AddBookTests(TestCase):
    def test_add_url_renders_add_book_form_template(self):
        response = self.client.get('/add/')
        self.assertTemplateUsed(response, 'add_book.html')

    def test_add_book_form_has_addbookform(self):
        response = self.client.get('/add/')
        self.assertIsInstance(response.context['form'], AddBookForm)

    def test_adding_a_book_redirects_to_book_view(self):
        response = self.client.post('/add-book/',
                                    data={'title': 'Harry Potter',
                                          'author_name': 'J.K. Rowling',
                                          'genre_name': 'Fantasy',
                                          'synopsis': 'Best Series Ever'},
                                    follow=True)
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        self.assertTemplateUsed(response, 'book.html')

    def test_adding_invalid_book_info_redirects_to_homepage(self):
        response = self.client.post('/add-book/',
                                    data={'title': '',
                                          'author_name': '',
                                          'genre_name': '',
                                          'synopsis': ''},
                                    follow=True)
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        self.assertTemplateUsed(response, 'homepage.html')

    def test_author_is_created_when_author_does_not_exist(self):
        count = Author.objects.count()
        self.client.post('/add-book/',
                         data={'title': 'Harry Potter',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever'},
                         follow=True)
        self.assertEqual(Author.objects.count(), count + 1)

    def test_author_is_NOT_created_when_author_already_exists_in_archive(self):
        self.client.post('/add-book/',
                         data={'title': 'Harry Potter',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever'},
                         follow=True)
        count = Author.objects.count()

        self.client.post('/add-book/',
                         data={'title': 'The Silkworm',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Mystery',
                               'synopsis': 'Currently reading..'},
                         follow=True)
        self.assertEqual(Author.objects.count(), count)

    def test_genre_is_created_when_genre_does_not_exist(self):
        count = Genre.objects.count()
        self.client.post('/add-book/',
                         data={'title': 'Harry Potter',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever'},
                         follow=True)
        self.assertEqual(Genre.objects.count(), count + 1)

    def test_genre_is_NOT_created_when_genre_already_exists_in_archive(self):
        self.client.post('/add-book/',
                         data={'title': 'Harry Potter',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever'},
                         follow=True)
        count = Genre.objects.count()

        self.client.post('/add-book/',
                         data={'title': 'The Lies of Locke Lamora',
                               'author_name': 'Scott Lynch',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Very good'},
                         follow=True)
        self.assertEqual(Genre.objects.count(), count)

    def test_cannot_add_book_that_is_already_in_the_database(self):
        self.client.post('/add-book/',
                         data={'title': 'Harry Potter',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever'},
                         follow=True)
        count = Genre.objects.count()

        self.client.post('/add-book/',
                         data={'title': 'Harry Potter',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever'},
                         follow=True)
        self.assertEqual(Genre.objects.count(), count)


class ListTests(TestCase):
    def test_list_books_renders_correct_template(self):
        response = self.client.get('/list-books/')
        self.assertTemplateUsed(response, 'list_books.html')

    def test_list_authors_renders_correct_template(self):
        response = self.client.get('/list-authors/')
        self.assertTemplateUsed(response, 'list_authors.html')

    def test_list_genres_renders_correct_template(self):
        response = self.client.get('/list-genres/')
        self.assertTemplateUsed(response, 'list_genres.html')

    def test_book_is_listed_after_it_is_added(self):
        self.client.post('/add-book/',
                         data={'title': 'Harry Potter',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever'},
                         follow=True)
        response = self.client.get('/add/')

        self.client.post('/add-book/',
                         data={'title': 'The Lies of Locke Lamora',
                               'author_name': 'Scott Lynch',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Very good'},
                         follow=True)
        response = self.client.get('/list-books/')
        self.assertContains(response, 'The Lies of Locke Lamora')
        self.assertContains(response, 'Harry Potter')

    def test_author_is_listed_after_they_are_added(self):
        self.client.post('/add-book/',
                         data={'title': 'Harry Potter',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever'},
                         follow=True)
        self.client.post('/add-book/',
                         data={'title': 'The Silkworm',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Mystery',
                               'synopsis': 'Currently reading..'},
                         follow=True)

        self.client.post('/add-book/',
                         data={'title': 'The Lies of Locke Lamora',
                               'author_name': 'Scott Lynch',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Very good'},
                         follow=True)

        response = self.client.get('/list-books/')
        self.assertContains(response, 'Scott Lynch')
        self.assertContains(response, 'J.K. Rowling')
        self.assertContains(response, 'The Lies of Locke Lamora')
        self.assertContains(response, 'Harry Potter')
        self.assertContains(response, 'The Silkworm')

    def test_genre_is_listed_after_it_is_added(self):
        self.client.post('/add-book/',
                         data={'title': 'Harry Potter',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever'},
                         follow=True)

        self.client.post('/add-book/',
                         data={'title': 'The Lies of Locke Lamora',
                               'author_name': 'Scott Lynch',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Very good'},
                         follow=True)
        self.client.post('/add-book/',
                         data={'title': 'The Silkworm',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Mystery',
                               'synopsis': 'Currently reading..'},
                         follow=True)

        response = self.client.get('/list-genres/')
        self.assertContains(response, 'Fantasy')
        self.assertContains(response, 'Mystery')
        self.assertContains(response, 'The Lies of Locke Lamora')
        self.assertContains(response, 'Harry Potter')
        self.assertContains(response, 'The Silkworm')
