from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('add-post/', views.add_post, name='add_post'),
]