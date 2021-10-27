from django import forms
from .models import BlogPost, BlogComments


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = '__all__'


class BlogCommentForm(forms.ModelForm):
    
    class Meta:
        model = BlogComments
        fields = [
            'author_comment',
            'main_comment',
        ]
