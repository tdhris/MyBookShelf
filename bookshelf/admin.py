from django.contrib import admin
from bookshelf.models import Author, Book, Genre, BookReview


class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'biography')


class BookAdmin(admin.ModelAdmin):

    class Meta:
        model = Book


class GenreAdmin(admin.ModelAdmin):
    fields = ('name', 'description')


class BookReviewAdmin(admin.ModelAdmin):
    class Meta:
        model = BookReview


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookReview, BookReviewAdmin)
