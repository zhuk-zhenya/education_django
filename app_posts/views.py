from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from . import models


# Create your views here.


def get_posts(request):
    posts = models.Post.objects.all()
    tags = models.Tag.objects.all()
    category_posts = models.CategoryPost.objects.all()
    context = {
        'posts': posts,
        'tags': tags,
        'category_posts': category_posts
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


def add_post(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "add_post.html", context={"form": form})
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("<h1>Что то пошло не так))</h1>")
    return redirect("get_posts")


def search_post(request):
    post = request.GET['title']
    category = request.GET['category']
    posts = models.Post.objects.all()
    if post != '':
        posts = posts.filter(title__contains=post)
    if category != '':
        posts = posts.filter(category_post__title__contains=category)

    return render(request, 'search_post.html', context={"posts": posts})


def delete_post(request, id):
    try:
        post = models.Post.objects.get(id=id)
    except models.Post.DoesNotExist:
        return HttpResponse(f"<h1> Поста с таким {id} не существует</h1>")
    post.delete()

    return redirect("get_posts")
