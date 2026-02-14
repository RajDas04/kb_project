from django import forms
from .models import Article
from ckeditor.widgets import CKEditorWidget
from taggit.forms import TagWidget

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags':TagWidget(attrs={'class':'form-control'}),
        }