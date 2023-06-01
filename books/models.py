from django.db import models


# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"Tag: {self.id}, {self.title}"


class Publisher(models.Model):
    LANGUAGES = (
        ("ru", "Russian"),
        ("en", "English"),
        ("fr", "French")
    )
    title = models.CharField(max_length=50)
    language = models.CharField(max_length=2, choices=LANGUAGES, default="ru")

    def __str__(self):
        return f"Publisher: {self.title} {self.language}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
    raiting = models.IntegerField(default=0)
    publisher = models.OneToOneField("Publisher", on_delete=models.DO_NOTHING, default=None)
    genre = models.ForeignKey("Genre", on_delete=models.DO_NOTHING, null=True, blank=True, related_name="books")
    tags = models.ManyToManyField("Tag", related_name="books")

    def __str__(self):
        return f"Book title: {self.title} Author: {self.author}"


    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
class Genre(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"Genre: {self.id}, {self.title}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    year = models.IntegerField()
    rating = models.IntegerField(default=0)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="movies")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="movies")

    def __str__(self):
        return f"Movie title: {self.title} Director: {self.director}"
