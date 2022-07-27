from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime


class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, blank=True)

    blog = models.TextField()
    pub_date = models.DateField(auto_now_add=True, blank=True)
    blog_img = models.ImageField(null=True, upload_to="blogpost_imgs/")

    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    tags = models.CharField(max_length=100, default="data analytics,data engineering, data science")

    def __str__(self):
        return f"Blog: {self.blog_title}"

    def tags_list(self):
        return self.tags.split(',')


class BlogImage(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blogpost_imgs/", blank=True, null=True)

    def __str__(self):
        return f"Image {self.image} for {self.blog}"


class Comment(models.Model):
    your_name = models.CharField(max_length=20, default="Anonymous")
    email = models.EmailField(max_length=150)
    comment_text = models.TextField()
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Comment by Name: {self.your_name}"


class Author(models.Model):
    author = models.CharField(max_length=100)
    author_desc = models.CharField(max_length=200, null=True)

    twitter = models.CharField(max_length=200, default="#")
    facebook = models.CharField(max_length=200, default="#")
    instagram = models.CharField(max_length=200, default="#")

    def __str__(self):
        return self.author


class Category(models.Model):
    category = models.CharField(max_length=50, default="Other")

    def __str__(self):
        return self.category

