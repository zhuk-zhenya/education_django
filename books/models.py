from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f"Book title: {self.title} Author: {self.author}"


class Genre(models.Model):
    title = models.CharField(max_length=50)
