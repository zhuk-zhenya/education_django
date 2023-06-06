from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_posts, name="get_posts"),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('tags/<int:pk>/', views.tag_detail, name='tag_detail'),
]
