from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
   # title = forms.CharField(label="标题",max_length=100)
   # content = forms.CharField(label="内容",max_length=1000)
    class Meta:
        model = Article
        fields = ['title','content']
