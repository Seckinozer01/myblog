from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import SupportForm
from .models import SupportMessage 
from django.contrib import messages
from myblog.settings import AUTH_USER_MODEL 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from user.models import Account
# Create your views here.

#---------------------------------------------------------------------------------------------------------#

def index(request):
    return render (request,"index.html")
#---------------------------------------------------------------------------------------------------------#

def contact(request):
    form = SupportForm(request.POST or None)
    if form.is_valid():
        support_message = form.save(commit = False)
        
        support_author = SupportMessage.support_name
        
        support_content = SupportMessage.support_content
        support_phone = SupportMessage.support_phone
        support_email = SupportMessage.support_email
        support_message.save()

        messages.success(request,"Mesaj Başarıyla Oluşturuldu")
        return redirect("contact")

    return render(request,"contact.html",{"form" : form})

#---------------------------------------------------------------------------------------------------------#  

def about(request):
        return render (request,"about.html")

