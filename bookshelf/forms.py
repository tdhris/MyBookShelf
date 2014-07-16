from django import forms
from django.forms import extras
from bookshelf.models import Author, Book


class SearchBookForm(forms.Form):
    title = forms.CharField(max_length=30)


class SearchAuthorForm(forms.models.ModelForm):
    class Meta:
        model = Author
        exclude = ['title', 'genre', 'pub_date']
        widgets = {'author': forms.fields.TextInput(attrs={
                   'placeholder': 'Search for author'})}


class AddBookForm(forms.models.ModelForm):
    class Meta:
        model = Book
        exclude = ['author', 'genre', 'pub_date']

    author_name = forms.CharField(max_length=30)
    genre_name = forms.CharField(max_length=30)
    publication_date = forms.DateField(widget=extras.SelectDateWidget(
        years=range(1930, 2014))
    )
