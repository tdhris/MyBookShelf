from django import forms
from bookshelf.models import Author


class SearchBookForm(forms.Form):
    title = forms.CharField(max_length=30)


class SearchAuthorForm(forms.models.ModelForm):
    class Meta:
        model = Author
        exclude = ['title', 'genre', 'pub_date']
        widgets = {'author': forms.fields.TextInput(attrs={
                   'placeholder': 'Search for author'})}
