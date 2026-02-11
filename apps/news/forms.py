from django import forms 
from apps.news.models import Comment, News


class NewsCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'category', 'image', 'description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']