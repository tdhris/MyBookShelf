from django.db import models
from django.core.urlresolvers import reverse


class Author(models.Model):
    name = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=30, default='')
    author = models.ForeignKey(Author)
    genre = models.ForeignKey(Genre)
    pub_date = models.DateField(auto_now_add=True)
    synopsis = models.TextField(default='')

    def get_absolute_url(self):
        return reverse('see_book', args=[self.id])

    def __str__(self):
        return self.title
