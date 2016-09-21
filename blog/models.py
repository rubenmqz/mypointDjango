from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post (models.Model):

    owner = models.ForeignKey(User)
    title = models.CharField(max_length=140)
    imgURL = models.URLField(null=True, blank=True)
    videoURL = models.URLField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    body = models.TextField()
    publish_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

