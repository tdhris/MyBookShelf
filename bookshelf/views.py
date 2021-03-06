from django.shortcuts import render, redirect, get_object_or_404
from bookshelf.forms import (SearchBookForm, AddBookForm,
                             EditAuthorForm, PostReviewForm,
                             EditGenreForm)
from bookshelf.models import Book, Author, Genre, BookReview
from collections import OrderedDict
from random import sample


def home_page(request):
    form = SearchBookForm()
    books = get_random(Book.objects.all(), 5)
    authors = get_random(Author.objects.all(), 5)
    genres = get_random(Genre.objects.all(), 5)
    return render(request, 'homepage.html', locals())


def get_random(objects, number):
    count = len(objects)
    if count:
        random_indexes = sample(range(len(objects)), number)
        random_objects = [objects[random_index] for random_index in random_indexes]
        return random_objects


def see_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    other_books = set(Book.objects.filter(author=book.author).exclude(title=book.title))
    other_books = other_books.union(Book.objects.filter(genre=book.genre).exclude(title=book.title))
    return render(request, 'book.html', locals())


def see_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    genres = set([book.genre for book in author.book_set.all()])
    return render(request, 'author.html', locals())


def edit_author(request, author_id):
    form = EditAuthorForm()
    return render(request, 'edit_author.html', locals())


def save_edit_author(request, author_id):
    form = EditAuthorForm(data=request.POST)
    if form.is_valid():
        new_biography = form.cleaned_data.get('biography')
        author = get_object_or_404(Author, pk=author_id)
        author.biography = new_biography
        author.save()
        return redirect(author)

    else:
        return render(request, 'homepage.html', {'form': SearchBookForm()})


def edit_genre(request, genre_id):
    form = EditGenreForm()
    return render(request, 'edit_genre.html', locals())


def save_edit_genre(request, genre_id):
    form = EditGenreForm(data=request.POST)
    if form.is_valid():
        genre = get_object_or_404(Genre, pk=genre_id)
        genre.name = form.cleaned_data.get('name')
        genre.description = form.cleaned_data.get('description')
        genre.save()
        return redirect(genre)

    else:
        return render(request, 'homepage.html', {'form': SearchBookForm()})


def see_genre(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    return render(request, 'genre.html', locals())


def add_book_form(request):
    form = AddBookForm()
    return render(request, 'add_book.html', locals())


def add_book(request):
    form = AddBookForm(data=request.POST)
    if form.is_valid():
        book_author = get_author_of_book(request.POST['author_name'])
        book_genre = get_genre_of_book(request.POST['genre_name'])
        book = Book.objects.create(title=form.cleaned_data.get('title'),
                                   author=book_author,
                                   genre=book_genre,
                                   synopsis=form.cleaned_data.get('synopsis'),
                                   pub_date=form.cleaned_data.get('publication_date'))
        return redirect(book)

    else:
        return render(request, 'homepage.html', {'form': SearchBookForm()})


def get_book(request):
    books = Book.objects.filter(title=request.POST['title'])
    if len(books) < 1:
        return add_book_form(request)
    else:
        wanted_book = books[0]
        return redirect(wanted_book)


def list_books(request):
    alphabetic_books = get_alphabetic_dictionary(Book.objects.all())
    return render(request, 'list_books.html', locals())


def high_rated_books(request):
    rated_books = [book for book in Book.objects.all()
                   if book.rating() != BookReview.NO_RATING]
    highly_rated_books = sorted(rated_books,
                                key=lambda book: book.rating(),
                                reverse=True)
    return render(request, 'highest_rated_books.html', locals())


def list_authors(request):
    alphabetic_authors = get_alphabetic_dictionary(Author.objects.all())
    return render(request, 'list_authors.html', locals())


def list_genres(request):
    alphabetic_genres = get_alphabetic_dictionary(Genre.objects.all())
    return render(request, 'list_genres.html', locals())


def get_author_of_book(author_name):
    authors = Author.objects.filter(name=author_name)
    if len(authors) < 1:
        author = Author.objects.create(name=author_name)
        return author
    else:
        return authors[0]


def get_genre_of_book(genre_name):
    genres = Genre.objects.filter(name=genre_name)
    if len(genres) < 1:
        genre = Genre.objects.create(name=genre_name)
        return genre
    else:
        return genres[0]


def about(request):
    book_count = Book.objects.count()
    author_count = Author.objects.count()
    genre_count = Genre.objects.count()
    return render(request, 'about.html', locals())


def get_alphabetic_dictionary(objects):
    objects = sorted(objects)
    alphabetic_dictionary = {first_letter:
                             [object for object in objects
                              if str(object).startswith(first_letter)]
                             for first_letter in set(str(object)[0]
                                                     for object in objects)}
    return OrderedDict(sorted(alphabetic_dictionary.items(), key=lambda t: t[0]))


def post_review(request, book_id):
    form = PostReviewForm()
    return render(request, 'post_review.html', locals())


def save_review(request, book_id):
    form = PostReviewForm(data=request.POST)
    if form.is_valid():
        book = Book.objects.get(pk=book_id)
        BookReview.objects.create(text=form.cleaned_data.get('text'),
                                  reviewer=get_user(request),
                                  score=form.cleaned_data.get('score'),
                                  book=book)
        return redirect(book)

    else:
        return render(request, 'homepage.html', {'form': SearchBookForm()})


def get_user(request):
    if request.user.is_authenticated():
        return request.user
