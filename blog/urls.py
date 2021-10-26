from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_post_page, name='blog_post_page'),
    path('upload_blog/', views.upload_blog, name='upload_blog'),
    path('edit_blog/<int:blog_id>', views.edit_blog, name='edit_blog'),
    path('delete_blog/<int:blog_id>', views.delete_blog, name='delete_blog'),
    path('full_post/<int:blog_id>', views.full_post, name='full_post'),
]
