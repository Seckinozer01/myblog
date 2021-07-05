from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import Hesap
from django.contrib.auth import authenticate


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length =60,help_text = "Bu Alanı Doldurunuz." )

    class Meta :
        model = Hesap
        fields = ("email","username","password1","password2")



class LoginForm(forms.ModelForm):
    password = forms.CharField(label = "Parola",widget = forms.PasswordInput)
    

    class Meta : 
        model = Hesap
        fields = ("email","password",)

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email = email,password=password):
                raise forms.ValidationError("Giriş Yapılamadı Lütfen Tekrar Deneyin")

