from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


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

    def get_absolute_url(self):
        return reverse('see_author', args=[self.id])


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


class Review(models.Model):
    ONE_STAR = 1
    TWO_STARS = 2
    THREE_STARS = 3
    FOUR_STARS = 4
    FIVE_STARS = 5
    REVIEW_SCORES = (
        (ONE_STAR, ONE_STAR),
        (TWO_STARS, TWO_STARS),
        (THREE_STARS, THREE_STARS),
        (FOUR_STARS, FOUR_STARS),
        (FIVE_STARS, FIVE_STARS))

    text = models.TextField(default='')
    reviewer = models.ForeignKey(User, blank=True, null=True)
    date = models.DateField(default=datetime.now(),
                            null=True, blank=True)
    score = models.IntegerField(choices=REVIEW_SCORES,
                                default=THREE_STARS,)

    def short(self):
        return self.text[:100]

    def __str__(self):
        return "Review by {0}".format(self.reviewer.username)


class BookReview(Review):
    book = models.ForeignKey(Book)

    def __eq__(self, other):
        return all([self.reviewer == other.reviewer,
                   self.score == other.score,
                   self.book == other.book])

    def __str__(self):
        return "Review of {0}".format(self.book.title)
