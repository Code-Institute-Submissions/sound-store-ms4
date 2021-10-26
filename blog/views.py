from django.shortcuts import render
from .models import BlogPost
from .forms import BlogForm

def blog_post_page(request):
    """Render the blog in the browser"""
    blogs = BlogPost.objects.all()

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog.html', context)


def upload_blog(request):
    form = BlogForm()
    template = 'blog/upload_blog.html'

    context = {
        'form': form,
    }

    return render(request, template, context)
