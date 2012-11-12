from django.db import models

from django.contrib.auth.models import User


class Postable(models.Model):

    poster = models.ForeignKey(User)
    body = models.TextField(verbose_name="Body (Markdown-formatted)")
    datetime_posted = models.DateTimeField(
        verbose_name="Date/Time posted (blank to use the current date/time)")

    class Meta:
        abstract = True
        ordering = ["-datetime_posted"]


class Post(Postable):

    title = models.CharField(max_length=255)


class Comment(Postable):

    post = models.ForeignKey(Post, related_name="comments")
