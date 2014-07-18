from django import forms
from django.forms import extras
from bookshelf.models import Author, Book, BookReview


class SearchBookForm(forms.Form):
    # def __init__(self, placeholder=None):
    #     super(SearchBookForm, self).__init__(self)
    #     if placeholder:

    title = forms.CharField(max_length=30)


class SearchAuthorForm(forms.models.ModelForm):
    class Meta:
        model = Author
        exclude = ['title', 'genre', 'pub_date']
        widgets = {'author': forms.fields.TextInput(attrs={
                   'placeholder': 'Search for author'})}


class AddBookForm(forms.models.ModelForm):
    author_name = forms.CharField(max_length=30)
    genre_name = forms.CharField(max_length=30)
    publication_date = forms.DateField(widget=extras.SelectDateWidget(
        years=range(1530, 2016))
    )

    class Meta:
        model = Book
        exclude = ['author', 'genre', 'pub_date']


class EditAuthorForm(forms.Form):
    biography = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 10}))


class PostReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        exclude = ['reviewer', 'date', 'book']
