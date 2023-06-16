from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_posts, name="get_posts"),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('tags/<int:pk>/', views.tag_detail, name='tag_detail'),
    path('create_post', views.add_post, name='create_post'),
    path('search_post/', views.search_post, name='search_post'),
    path('delete_post/<int:id>/', views.delete_post, name="delete_book"),


]
