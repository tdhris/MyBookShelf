from django.shortcuts import render, redirect, get_object_or_404
from bookshelf.forms import SearchBookForm, AddBookForm
from bookshelf.models import Book, Author, Genre


def home_page(request):
    form = SearchBookForm()
    return render(request, 'homepage.html', locals())


def see_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book.html', locals())


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
        return render(request, 'book_not_found.html')
    else:
        wanted_book = books[0]
        return redirect(wanted_book)


def list_books(request):
    books = sorted(Book.objects.all())
    return render(request, 'list_books.html', locals())


def list_authors(request):
    authors = sorted(Author.objects.all())
    return render(request, 'list_authors.html', locals())


def list_genres(request):
    genres = sorted(Genre.objects.all())
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
