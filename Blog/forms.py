from django import forms
from .models import Articles,Category



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ["title","category","content","article_image",]

        


