from django.shortcuts import render
from .models import BlogPost


def BlogPostPage(request):
    blogs = BlogPost.objects.all()

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog.html', context)
