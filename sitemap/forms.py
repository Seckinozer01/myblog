from django import forms
from .models import SupportMessage




class SupportForm(forms.ModelForm):
    class Meta:
        model = SupportMessage
        fields = ["support_name","support_email","support_phone","support_content",]