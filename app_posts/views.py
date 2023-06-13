from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from . import models


# Create your views here.


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


def add_post(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "add_post.html", context={"form": form})
    elif request.method == "POST":

        post = models.Post.objects.create(title=request.POST['title'],
                                          category=request.POST['category'],
                                          description=request.POST['description'],
                                          created_date=request.POST['created_date'],
                                          )
        tags = request.POST.getlist('tags')
        post.tags.set(tags)
        post.save()

        return redirect("get_posts")


def search_post(request):
    search_query = request.GET['search']
    print(search_query)
    search_posts = models.Post.objects.filter(title__contains=search_query)

    return render(request, 'search_post.html', context={"posts": search_posts})
