from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

'''
posts = [
    {
        'author': 'Caroline',
        'title': 'Blog Post',
        'content': 'first post'
    },
    {
        'author': 'Shelly',
        'title': 'Blog Post',
        'content': 'first post'
    }
]
'''


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
