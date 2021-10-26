from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'blog_created',
        'blog_title',
        'blog_author',
        'blog_updated'
    )

    list_filter = ('blog_created',)

    search_fields = ['blog_title', 'blog_created']

    ordering = ['-blog_created']


admin.site.register(BlogPost, BlogPostAdmin)
