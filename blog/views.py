from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogForm


def blog_post_page(request):
    """Render the blog in the browser"""
    blogs = BlogPost.objects.all()

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog.html', context)

@login_required
def upload_blog(request):
    """Upload a blog to the database, admin only"""
    if not request.user.is_superuser:
        messages.error(request, 'Only admin can upload a blog.')
        return redirect(reverse('blog_post_page'))

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

@login_required
def edit_blog(request, blog_id):
    """Edit a blog, admin only"""
    if not request.user.is_superuser:
        messages.error(request, 'Only admin can edit a blog.')
        return redirect(reverse('blog_post_page'))

    blog = get_object_or_404(BlogPost, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog updated.')
            return redirect(reverse('blog_post_page'))
        else:
            messages.error(request, 'Blog was not edited. Pease ensure \
                you have filled the form out correctly')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'Updating {blog.blog_title}')

    template = 'blog/edit_blog.html'

    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)

@login_required
def delete_blog(request, blog_id):
    """Delete a blog from database, admin only"""
    if not request.user.is_superuser:
        messages.error(request, 'Only admin can delete a blog.')
        return redirect(reverse('blog_post_page'))
    blog = get_object_or_404(BlogPost, pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog has been deleted')
    return redirect(reverse('blog_post_page'))


def full_post(request, blog_id):
    blogs = get_object_or_404(BlogPost, pk=blog_id)

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/full_blog.html', context)
