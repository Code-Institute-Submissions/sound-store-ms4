from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
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
    """Upload a blog to the database"""
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog uploaded to site.')
            return redirect(reverse('blog_post_page'))
        else:
            messages.error(request, 'Blog not uploaded, please ensure the form \
                 is filled out correctly')
    else:
        form = BlogForm()
    template = 'blog/upload_blog.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_blog(request, blog_id):
    """Edit a blog"""
    blog = get_object_or_404(BlogPost, pk=blog_id)
    form = BlogForm(instance=blog)
    messages.info(request, f'Updating {blog.blog_title}')

    template = 'blog/edit_blog.html'

    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)
