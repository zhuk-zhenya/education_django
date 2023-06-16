from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
from .forms import BookForm


# Create your views here.


def books(request):
    books = models.Book.objects.all()
    genres = models.Genre.objects.all()
    publishers = models.Publisher.objects.all()
    return render(request, "index.html", context={"books": books,
                                                  "genres": genres,
                                                  "publishers": publishers})


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


def get_tag_books(request, title):
    try:
        tag = models.Tag.objects.get(title=title)
    except models.Genre.DoesNotExist:
        return HttpResponse(f"<h1>{title} не существует! </h1>")

    tag_books = tag.books.all()
    return render(request, "tag_book_detail.html", context={"tag_books": tag_books,
                                                            "tag": tag})


def add_book(request):
    if request.method == "GET":
        form = BookForm()
        return render(request, "add_book.html", context={"form": form})
    elif request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("<h1>Что то пошло не так))</h1>")
    return redirect("books")

        # if publisher_id != '' and genre_id != '':
        #     publisher = models.Publisher.objects.get(id=publisher_id)
        #     genre = models.Genre.objects.get(id=genre_id)
        # else:
        #     publisher = None
        #     genre = None
        #
        # book = models.Book.objects.create(title=request.POST['title'],
        #                                   author=request.POST['author'],
        #                                   year=request.POST['year'],
        #                                   raiting=request.POST['raiting'],
        #                                   publisher=publisher,
        #                                   genre=genre)
        # tags = request.POST.getlist('tags')
        # book.tags.set(tags)
        # book.save()
        #
        # return redirect("books")


def search_book(request):
    title = request.GET['title']
    genre = request.GET['genre']
    books = models.Book.objects.all()
    if title != '':
        books = books.filter(title__contains=title)
    if genre != '':
        books = books.filter(genre__title__contains=genre)
    return render(request, 'search_book.html', context={"books": books})


def delete_book(request, id):
    try:
        book = models.Book.objects.get(id=id)
    except models.Book.DoesNotExist:
        return HttpResponse(f"<h1>книги с таким айди {id} не существует</h1>")
    book.delete()
    return redirect('books')
