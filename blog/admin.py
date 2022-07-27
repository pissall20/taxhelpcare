from django.contrib import admin

# Register your models here.
from .models import Blog, Comment, BlogImage, Author, Category
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(BlogImage)
admin.site.register(Author)
admin.site.register(Category)
