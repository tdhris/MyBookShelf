from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse


class Author(models.Model):
    name = models.CharField(max_length=30, default='')
    biography = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name

    def short(self):
        return self.biography[:100]


class Genre(models.Model):
    name = models.CharField(max_length=30, default='')
    description = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name

    def short(self):
        return self.description[:100]


class Book(models.Model):
    title = models.CharField(max_length=60, default='')
    author = models.ForeignKey(Author)
    genre = models.ForeignKey(Genre)
    pub_date = models.DateField('Publication Date',
                                default=datetime.now(),
                                null=True, blank=True)
    synopsis = models.TextField(default='')

    def get_absolute_url(self):
        return reverse('see_book', args=[self.id])

    def short(self):
        return self.synopsis[:100]

    def __str__(self):
        return self.title

    def __lt__(self, other):
        return self.title < other.title

    def __le__(self, other):
        return self.title <= other.title

    def __eq__(self, other):
        return all([self.title == other.title,
                    self.author == other.author,
                    self.genre == other.genre,
                    self.pub_date == other.pub_date])

    def __ne__(self, other):
        return not (self.__eq__(other))

    def __gt__(self, other):
        return self.title > other.title

    def __ge__(self, other):
        return self.title >= other.title
