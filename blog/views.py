from django.shortcuts import render

# Create your views here.
from .models import Blog, Comment
from .forms import SearchForm, CommentForm
from django.shortcuts import render, redirect
from django.http import Http404
from django.template import loader


def blog_list_view(request):
    blogs = Blog.objects.all().order_by("-pub_date")
    context = dict()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            blog = Blog.objects.get(blog_title=title)
            return redirect(f'/blog/{blog.id}')
    else:
        form = SearchForm()
        context = {
            'blogs': blogs,
            'form': form,
        }
    return render(request, 'blog/blog-list.html', context)


def blog_single_view(request):
    context = {}
    return render(request, 'blog/blog-single.html', context)


def blog_detail_view(request, _id):
    try:
        data = Blog.objects.get(id=_id)
        comments = Comment.objects.filter(blog=data)
    except Blog.DoesNotExist:
        raise Http404('Data does not exist')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user_comment = Comment(your_name=form.cleaned_data['your_name'],
                                   comment_text=form.cleaned_data['comment_text'],
                                   blog=data)
            user_comment.save()
            return redirect(f'/blog/{_id}')
    else:
        form = CommentForm()

    context = {
        'blog': data,
        'form': form,
        'comments': comments,
    }
    return render(request, 'blog/blog-page.html', context)
