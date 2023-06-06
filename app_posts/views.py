from django.shortcuts import render, get_object_or_404

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


def post_detail(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context=context)


def tag_detail(request, pk):
    tag = get_object_or_404(models.Tag, pk=pk)
    posts = tag.posts.all()
    context = {
        'tag': tag,
        'posts': posts,
    }
    return render(request, 'tag_detail.html', context=context)
