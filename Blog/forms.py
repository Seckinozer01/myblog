from django import forms
from .models import ShowArticle,SendSupport ,Category



class ArticleForm(forms.ModelForm):
    class Meta:
        model = ShowArticle
        fields = ["title","category","content","article_image",]

        


class SupportForm(forms.ModelForm):
    class Meta:
        model = SendSupport
        fields = ["support_name","support_email","support_phone","support_content","support_tittle"]