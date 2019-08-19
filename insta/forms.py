from insta.models import *
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('caption', 'image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        