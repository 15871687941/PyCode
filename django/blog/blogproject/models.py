from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

