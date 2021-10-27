from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    blog_title = models.CharField(max_length=200, null=False, blank=False)
    blog_author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name="blog_author")
    blog_slug = models.SlugField(max_length=200)
    blog_heading = models.CharField(max_length=400, null=False, blank=False)
    blog_main = models.TextField()
    blog_image_url = models.URLField(max_length=1000, null=True, blank=True)
    blog_image = models.ImageField(null=True, blank=True)
    blog_created = models.DateTimeField(auto_now_add=True)
    blog_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-blog_created']

    def __str__(self):
        return self.blog_title


class BlogComments(models.Model):

    class Meta:
        verbose_name_plural = 'Blog Comments'

    blog_comment = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="blog_post")
    author_comment = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name="author_comment")
    uploaded_comment = models.DateTimeField(auto_now_add=True)
    main_comment = models.TextField()

    def __str__(self):
        return self.author_comment
