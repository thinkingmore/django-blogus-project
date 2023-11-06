from django.shortcuts import render, get_object_or_404
from .models import Post,Category
from authentication.views import *

def index(request):
    # get published blog posts
    blog_posts = Post.objects.all()  

    context = {
        'post_list': blog_posts,
    }

    return render(request, "pages/index.html", context)

def post_detail(request, post_slug):
    # get post details  
    post = get_object_or_404(Post, slug=post_slug)

    return render(request, 'pages/post_detail.html', {'post': post})


def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(categories=category)

    return render(request, 'pages/category_posts.html', {'category': category, 'post_list': posts})