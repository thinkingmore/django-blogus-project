from django.shortcuts import render, get_object_or_404
from .models import Post,Category
from authentication.views import *
from .forms import AddPostForm


 # get published blog posts
def index(request):
    blog_posts = Post.objects.all()  

    context = {
        'post_list': blog_posts,
    }

    return render(request, "pages/index.html", context)


# get post details 
def post_detail(request, post_slug): 
    post = get_object_or_404(Post, slug=post_slug)

    return render(request, 'pages/post_detail.html', {'post': post})


def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(categories=category)

    return render(request, 'pages/category_posts.html', {'category': category, 'post_list': posts})



# add blog post  
def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', post_slug=post.slug) 
    else:
        form = AddPostForm()
    
    return render(request, 'pages/add_post.html', {'form': form})