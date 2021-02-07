from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.FileField()
    active = forms.BooleanField()
