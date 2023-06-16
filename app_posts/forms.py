from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'tags', 'category', 'description', 'created_date', 'category_post']
