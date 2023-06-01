from django.shortcuts import render
from . import models
# Create your views here.


def books(request):
    books = models.Book.objects.all()
    genres = models.Genre.objects.all()
    publishers = models.Publisher.objects.all()
    return render(request, "index.html", context={"books": books,
                                                  "genres": genres,
                                                  "publishers": publishers,
                                                  })

