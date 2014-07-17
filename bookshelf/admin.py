from django.contrib import admin
from bookshelf.models import Author, Book, Genre


class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'biography')


class BookAdmin(admin.ModelAdmin):

    class Meta:
        model = Book


class GenreAdmin(admin.ModelAdmin):
    fields = ('name', 'description')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
