from django import forms
from .models import Post, Comment

# 게시물 form
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['photo', 'body']

# 댓글 form
class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment 
        fields = ['comment']