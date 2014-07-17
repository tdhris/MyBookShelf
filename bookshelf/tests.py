from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import home_page, get_alphabetic_dictionary
from .forms import SearchBookForm, AddBookForm
from .models import Book, Author, Genre
from datetime import date
import unittest

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
    def test_get_book_redirects_to_add_book_when_book_does_not_exist(self):
        response = self.client.post('/get/', data={'title': "Blah Blah Book"})
        self.assertTemplateUsed(response, 'add_book.html')

    def test_get_book_redirects_book_page_when_book_exists_in_database(self):
        jkrowling = Author.objects.create(name='J.K. Rowling')
        fantasy = Genre.objects.create(name='Fantasy')
        Book.objects.create(title='Harry Potter', author=jkrowling,
                            genre=fantasy, synopsis='Best Series Ever')
        response = self.client.post('/get/', data={'title': 'Harry Potter'},
                                    follow=True)
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        self.assertTemplateUsed(response, 'book.html')


class AddBookTests(TestCase):
    def test_add_url_renders_add_book_form_template(self):
        response = self.client.get('/add/')
        self.assertTemplateUsed(response, 'add_book.html')

    def test_add_book_form_has_addbookform(self):
        response = self.client.get('/add/')
        self.assertIsInstance(response.context['form'], AddBookForm)

    def test_a_book_is_added_to_the_database(self):
        count = Book.objects.count()
        self.client.post('/add-book/',
                         data={'title': 'Harry Potter',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever',
                               'publication_date': date.today()},
                         follow=True)
        self.assertEqual(Book.objects.count(), count + 1)

    def test_adding_a_book_redirects_to_book_view(self):
        response = self.client.post('/add-book/',
                                    data={'title': 'Harry Potter',
                                          'author_name': 'J.K. Rowling',
                                          'genre_name': 'Fantasy',
                                          'synopsis': 'Best Series Ever',
                                          'publication_date': date.today()},
                                    follow=True)
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        self.assertTemplateUsed(response, 'book.html')

    def test_adding_invalid_book_info_redirects_to_homepage(self):
        response = self.client.post('/add-book/',
                                    data={'title': '',
                                          'author_name': '',
                                          'genre_name': '',
                                          'synopsis': '',
                                          'publication_date': date.today()},
                                    follow=True)
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        self.assertTemplateUsed(response, 'homepage.html')

    def test_a_book_is_not_added_if_title_has_more_than_60_letters(self):
        count = Book.objects.count()
        self.client.post('/add-book/',
                         data={'title': 'Harry Potter Blalallalala\
                                         lallalallala lallalalal\
                                         fsfdfdsfdgs lalalalalal allaal',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever',
                               'publication_date': date.today()},
                         follow=True)
        self.assertEqual(Book.objects.count(), count)

    def test_author_is_created_when_author_does_not_exist(self):
        count = Author.objects.count()
        self.client.post('/add-book/',
                         data={'title': 'Harry Potter',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever',
                               'publication_date': date.today()},
                         follow=True)
        self.assertEqual(Author.objects.count(), count + 1)

    def test_author_is_NOT_created_when_author_already_exists_in_archive(self):
        self.client.post('/add-book/',
                         data={'title': 'Harry Potter',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever',
                               'publication_date': date.today()},
                         follow=True)
        count = Author.objects.count()

        self.client.post('/add-book/',
                         data={'title': 'The Silkworm',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Mystery',
                               'synopsis': 'Currently reading..',
                               'publication_date': date.today()},
                         follow=True)
        self.assertEqual(Author.objects.count(), count)

    def test_genre_is_created_when_genre_does_not_exist(self):
        count = Genre.objects.count()
        self.client.post('/add-book/',
                         data={'title': 'Harry Potter',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever',
                               'publication_date': date.today()},
                         follow=True)
        self.assertEqual(Genre.objects.count(), count + 1)

    def test_genre_is_NOT_created_when_genre_already_exists_in_archive(self):
        self.client.post('/add-book/',
                         data={'title': 'Harry Potter',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever',
                               'publication_date': date.today()},
                         follow=True)
        count = Genre.objects.count()

        self.client.post('/add-book/',
                         data={'title': 'The Lies of Locke Lamora',
                               'author_name': 'Scott Lynch',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Very good',
                               'publication_date': date.today()},
                         follow=True)
        self.assertEqual(Genre.objects.count(), count)

    def test_cannot_add_book_that_is_already_in_the_database(self):
        self.client.post('/add-book/',
                         data={'title': 'Harry Potter',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever',
                               'publication_date': date.today()},
                         follow=True)
        count = Genre.objects.count()

        self.client.post('/add-book/',
                         data={'title': 'Harry Potter',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever',
                               'publication_date': date.today()},
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
                               'synopsis': 'Best Series Ever',
                               'publication_date': date.today()},
                         follow=True)
        response = self.client.get('/add/')

        self.client.post('/add-book/',
                         data={'title': 'The Lies of Locke Lamora',
                               'author_name': 'Scott Lynch',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Very good',
                               'publication_date': date.today()},
                         follow=True)
        response = self.client.get('/list-books/')
        self.assertContains(response, 'The Lies of Locke Lamora')
        self.assertContains(response, 'Harry Potter')

    def test_author_is_listed_after_they_are_added(self):
        self.client.post('/add-book/',
                         data={'title': 'Harry Potter',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever',
                               'publication_date': date.today()},
                         follow=True)
        self.client.post('/add-book/',
                         data={'title': 'The Silkworm',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Mystery',
                               'synopsis': 'Currently reading..',
                               'publication_date': date.today()},
                         follow=True)

        self.client.post('/add-book/',
                         data={'title': 'The Lies of Locke Lamora',
                               'author_name': 'Scott Lynch',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Very good',
                               'publication_date': date.today()},
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
                               'synopsis': 'Best Series Ever',
                               'publication_date': date.today()},
                         follow=True)

        self.client.post('/add-book/',
                         data={'title': 'The Lies of Locke Lamora',
                               'author_name': 'Scott Lynch',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Very good',
                               'publication_date': date.today()},
                         follow=True)
        self.client.post('/add-book/',
                         data={'title': 'The Silkworm',
                               'author_name': 'J.K. Rowling',
                               'genre_name': 'Mystery',
                               'synopsis': 'Currently reading..',
                               'publication_date': date.today()},
                         follow=True)

        response = self.client.get('/list-genres/')
        self.assertContains(response, 'Fantasy')
        self.assertContains(response, 'Mystery')
        self.assertContains(response, 'The Lies of Locke Lamora')
        self.assertContains(response, 'Harry Potter')
        self.assertContains(response, 'The Silkworm')

    def test_books_are_listed_in_alphabetic_order(self):
        self.client.post('/add-book/',
                         data={'title': 'A Game of Thrones',
                               'author_name': 'George R. R. Martin',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Best Series Ever',
                               'publication_date': date.today()},
                         follow=True)

        self.client.post('/add-book/',
                         data={'title': 'Billion Dollar Brain',
                               'author_name': 'Len Deighton',
                               'genre_name': 'Thriller',
                               'synopsis': 'Meh',
                               'publication_date': date.today()},
                         follow=True)

        self.client.post('/add-book/',
                         data={'title': 'The Spy',
                               'author_name': 'John le Carré',
                               'genre_name': 'Thriller',
                               'synopsis': 'Meh',
                               'publication_date': date.today()},
                         follow=True)

        books = self.client.get('/list-books/').context['alphabetic_books'].values()
        books = [book[0] for book in books]
        self.assertEqual('A Game of Thrones', books[0].title)
        self.assertEqual('Billion Dollar Brain', books[1].title)
        self.assertEqual('The Spy', books[2].title)

    def test_authors_are_listed_in_alphabetic_order(self):
        self.client.post('/add-book/',
                         data={'title': 'The Little Prince',
                               'author_name': 'Antoine de Saint-Exupéry',
                               'genre_name': 'Classics',
                               'synopsis': 'Best Series Ever',
                               'publication_date': date.today()},
                         follow=True)

        self.client.post('/add-book/',
                         data={'title': '1984',
                               'author_name': 'George Orwell',
                               'genre_name': 'Classics',
                               'synopsis': 'Awesome',
                               'publication_date': date.today()},
                         follow=True)

        self.client.post('/add-book/',
                         data={'title': 'The Hunger Games',
                               'author_name': 'Suzanne Collins',
                               'genre_name': 'Science Fiction',
                               'synopsis': 'Meh',
                               'publication_date': date.today()},
                         follow=True)

        authors = self.client.get('/list-authors/').context['alphabetic_authors'].values()
        authors = [author[0] for author in authors]
        self.assertEqual('Antoine de Saint-Exupéry', authors[0].name)
        self.assertEqual('George Orwell', authors[1].name)
        self.assertEqual('Suzanne Collins', authors[2].name)

    def test_genres_are_listed_in_alphabetic_order(self):
        self.client.post('/add-book/',
                         data={'title': 'The Little Prince',
                               'author_name': 'Antoine de Saint-Exupéry',
                               'genre_name': 'Classics',
                               'synopsis': 'Best Series Ever',
                               'publication_date': date.today()},
                         follow=True)

        self.client.post('/add-book/',
                         data={'title': 'A Game of Thrones',
                               'author_name': 'George Martin',
                               'genre_name': 'Fantasy',
                               'synopsis': 'Awesome',
                               'publication_date': date.today()},
                         follow=True)

        self.client.post('/add-book/',
                         data={'title': 'The Hunger Games',
                               'author_name': 'Suzanne Collins',
                               'genre_name': 'Science Fiction',
                               'synopsis': 'Meh',
                               'publication_date': date.today()},
                         follow=True)

        genres = self.client.get('/list-genres/').context['alphabetic_genres'].values()
        genres = [genre[0] for genre in genres]
        self.assertEqual('Classics', genres[0].name)
        self.assertEqual('Fantasy', genres[1].name)
        self.assertEqual('Science Fiction', genres[2].name)


class TestHelperFunctions(unittest.TestCase):
    def test_get_alphabetic_dictionary(self):
        strings = ['amazon', 'author', 'baba', 'baz', 'bor']
        alph_dict = get_alphabetic_dictionary(strings)
        self.assertEqual({'a': ['amazon', 'author'],
                          'b': ['baba', 'baz', 'bor']},
                         alph_dict)
