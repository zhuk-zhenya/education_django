from django.urls import path
from . import views

urlpatterns = [
    path("", views.books, name="books"),
    path("<int:id>", views.get_book, name="get_book"),
    path('<str:title>', views.get_genre_books, name="get_genre"),
    path('<str:title>', views.get_tag_books, name="get_tag_books"),
    path("add_book/", views.add_book, name="add_book"),
    # path('create_book/', views.create_book, name='create_book')
    path('search_book/', views.search_book, name="search_book"),
    path('delete_book/<int:id>/', views.delete_book, name="delete_post"),
]

