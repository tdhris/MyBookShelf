from django.shortcuts import render, redirect, get_object_or_404
from bookshelf.forms import SearchBookForm
from bookshelf.models import Book


def home_page(request):
    form = SearchBookForm()
    return render(request, 'homepage.html', {'form': form})


def see_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    render(request, 'book.html', {'book': book})


def get_book(request):
    book = Book.objects.filter(title=request.POST['title'])
    return redirect(book)
