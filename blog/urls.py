from django.urls import path

from . import views

urlpatterns = [
    path('blogs/', views.blog_list_view, name='blogs'),
    path('blogs/blog-single', views.blog_single_view, name='blog_single'),
    path('blog/<int:_id>', views.blog_detail_view, name='blog_post'),
]