from django.shortcuts import render , get_object_or_404
from .models import Post


def blog(request):
    total_post=Post.objects.count()
    posts=Post.objects.order_by('-published')
    return render(request,"blog.html", {"posts":posts, "total_post":total_post})


def post_details(request, slug):
    post=get_object_or_404(Post,slug=slug)
    return render(request,"post_detail.html",{'post':post})
