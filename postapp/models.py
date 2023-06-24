from django.db import models
from django.utils.timezone import now
from taggit.managers import TaggableManager

class Post(models.Model):
    postid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=now, blank=True)
    tags = TaggableManager()