from django.shortcuts import render

# Create your views here.
from . import models


def get_posts(request):
    posts = models.Post.objects.all()
    tags = models.Tag.objects.all()
    context = {
        'posts': posts,
        'tags': tags
    }
    return render(request, 'posts.html', context=context)
