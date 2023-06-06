from django.http import HttpResponse
from django.shortcuts import render
from . import models


# Create your views here.


def books(request):
    books = models.Book.objects.all()
    return render(request, "index.html", context={"books": books})


def get_book(request, id):
    # .all - все
    # .get - один
    # .filter - фильтр
    # .create - создать
    # .delete - удалить
    try:
        book = models.Book.objects.get(id=id)
    except models.Book.DoesNotExist:
        return HttpResponse(f"<h1>Книги с  id {id} не существует</h1>")

    return render(request, "detail.html", context={"book": book})


def get_genre_books(request, title):
    try:
        genre = models.Genre.objects.get(title=title)
    except models.Genre.DoesNotExist:
        return HttpResponse(f"<h1>Жанра с таким названием не существует! </h1>")

    return render(request, "genre.html", context={"genre": genre})
