from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
import datetime

from django.utils import timezone
import pytz

# managers
class BookmarkManager(models.Manager):
    def create_bookmark(self, url, time_of_now):
        bookmark = Bookmark(URL=url, posted_at=time_of_now)
        while True:
            bookmark.generate_code()
            if not self.code_duplicate(bookmark.code):
                break
        bookmark.save()
        return bookmark

    def code_duplicate(self, code):
        ret = False
        for b in self.all():
            if code == b.code:
                ret = True
                break
        return ret

# models
class Tag(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Bookmark(models.Model):
    URL = models.CharField(max_length=300)
    code = models.CharField(max_length=10, unique=True)
    posted_at = models.DateTimeField()
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    tag = models.ManyToManyField(Tag, blank=True)

    objects = BookmarkManager()

    def __str__(self):
        ret_st = ""
        if self.title is None:
            ret_st += self.title + ": "
        ret_st += self.URL
        return ret_st

    def generate_code(self):
        from random import choice
        from string import ascii_lowercase
        self.code = "".join(choice(ascii_lowercase) for _ in range(4))

    def total_clicks(self):
        return len(self.tag_set.all())


class Bookmarker(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField(null=True)
    gender_options = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, choices=gender_options, default='M')

    def __str__(self):
        return self.user.username


class Click(models.Model):
    bookmark = models.ForeignKey(Bookmark)
    user = models.ForeignKey(User, null=True)
    clicked_at = models.DateTimeField(null=True)

    def set_time(self):
        tzname = request.session.get('django_timezone')
        timezone.activate(pytz.timezone(tzname))
        self.clicked_at = timezone.now()
        timezone.deactivate()
