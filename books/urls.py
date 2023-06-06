from django.urls import path
from . import views

urlpatterns = [
    path("", views.books, name="books"),
    path("<int:id>", views.get_book, name="get_book"),
    path('<str:title>', views.get_genre_books, name="get_genre"),

]
