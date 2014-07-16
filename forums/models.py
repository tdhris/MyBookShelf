from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from operator import attrgetter


class Forum(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    @property
    def thread_count(self):
        return self.topic_set.count()

    @property
    def post_count(self):
        return sum(topic.post_count for topic in self.topic_set.all())

    def last_post(self):
        if self.topic_set.count():
            last_in_forum = None
            for topic in self.topic_set.all():
                last_in_topic = topic.last_post()
                if not last_in_forum:
                    last_in_forum = last_in_topic
                elif last_in_topic.date_created > last_in_forum.date_created:
                    last_in_forum = last_in_topic

            return last_in_forum

    def get_absolute_url(self):
        return reverse('forums.views.view_forum', args=[self.id])


class Topic(models.Model):
    title = models.CharField(max_length=70)
    date_created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    forum = models.ForeignKey(Forum)

    def __str__(self):
        return self.title

    @property
    def post_count(self):
        return self.post_set.count()

    def last_post(self):
        if self.post_set.count():
            return sorted(self.post_set.all(),
                          key=attrgetter('date_created'),
                          reverse=True)[0]

    def get_absolute_url(self):
        return reverse('forums.views.view_topic', args=[self.id])


class Post(models.Model):
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    poster = models.ForeignKey(User, blank=True, null=True)
    topic = models.ForeignKey(Topic)

    def __str__(self):
        return "posted in %s by %s" % (str(self.topic), str(self.poster))

    def short(self):
        return "'" + self.text[:10] + "' | " + str(self)
