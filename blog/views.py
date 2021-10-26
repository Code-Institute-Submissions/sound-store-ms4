from django.shortcuts import render


def BlogPostPage(request):
    return render(request, 'blog/blog.html')
