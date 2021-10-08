from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import ArticleForm
from .models import Articles,Comments,Category 
from django.contrib import messages
from myblog.settings import AUTH_USER_MODEL 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from user.models import Account
# Create your views here.
#---------------------------------------------------------------------------------------------------------#
def articles(request):
    keyword = request.GET.get("keyword")
    
    articles = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if keyword:
        articles = Articles.objects.filter(title__contains = keyword )
        return render(request,"index.html",{"articles":articles})
    if categoryID:
        articles = Articles.get_all_articles_by_categoryid(categoryID)
        if keyword:
            articles = Articles.objects.filter(title__contains = keyword)
            return render(request,"index/?category={{category.id}}",{"articles":articles})
    else:
        articles =  Articles.get_all_articles()
    data = {}
    data ['articles'] = articles
    data ['categories'] = categories
    return render (request,'articles.html',data)

    return render(request,"articles.html",{"articles":articles})
 #---------------------------------------------------------------------------------------------------------#   

def categorydetail(request,):
    keyword = request.GET.get("keyword")

    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if keyword:
        articles = Articles.objects.filter(title__contains = keyword )
        return render(request,"category.html",{"articles":articles , "categories": categories})
    if categoryID:
        articles = Articles.get_all_articles_by_categoryid(categoryID)
    else:
        articles =  Articles.get_all_articles()
    data = {}
    data ['articles'] = articles
    data ['categories'] = categories
    return render (request,'category.html',data)

    return render(request,"category.html",{"articles":articles})

#---------------------------------------------------------------------------------------------------------#

@login_required(login_url = "user:login")
def dashboard(request):
    
    articles = Articles.objects.filter(author = request.user)
    context = {"articles":articles}

    return render(request,"dashboard.html",context)
#---------------------------------------------------------------------------------------------------------#


@login_required(login_url = "user:login")
def admindashboard(request):
    
    articles = Articles.objects.filter(author = request.user)
    context = {"articles":articles}

    return render(request,"admin/admindashboard.html",context)

#---------------------------------------------------------------------------------------------------------#

@login_required(login_url = "user:login")
def adminarticles(request):
    keyword = request.GET.get("keyword")
    users = Account.get_all_users()
    articles = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if keyword:
        articles = Articles.objects.filter(title__contains = keyword )
        return render(request,"index.html",{"articles":articles})
    if categoryID:
        articles = Articles.get_all_articles_by_categoryid(categoryID)
        if keyword:
            articles = Articles.objects.filter(title__contains = keyword)
            return render(request,"index/?category={{category.id}}",{"articles":articles})
    else:
        articles =  Articles.get_all_articles()
    data = {}
    data ['articles'] = articles
    data ['categories'] = categories
    data ['users'] = users
    return render (request,'admin/generaladmin.html',data)

    return render(request,"admin/generaladmin.html",{"articles":articles},{"users":users})

#---------------------------------------------------------------------------------------------------------#
@login_required(login_url = "user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    
    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()

        messages.success(request,"Makale Başarıyla Oluşturuldu")
        return redirect("Article:dashboard")

    return render(request,"addarticle.html",{"form" : form})
#---------------------------------------------------------------------------------------------------------#
def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Articles,id=id)
    comments = article.comments.all()

    keyword = request.GET.get("keyword")
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    
    if categoryID:
        articles = Articles.get_all_articles_by_categoryid(categoryID)
        if keyword:
            articles = Articles.objects.filter(title__contains = keyword)
            return render(request,"index/?category={{category.id}}",{"articles":articles})
    else:
        articles = Articles.get_all_articles()
    data = {}
    data ['articles'] = articles
    data ['categories'] = categories
    return render (request,"detail.html",{"article":article,"comments":comments,"articles":articles , "categories":categories})
 #---------------------------------------------------------------------------------------------------------#   

@login_required(login_url = "user:login")
def updateArticle(request,id):
    article = get_object_or_404(Articles,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Makale başarıyla güncellendi")
        return redirect("Article:dashboard")


    return render(request,"update.html",{"form":form})
 #---------------------------------------------------------------------------------------------------------#   
@login_required(login_url = "user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Articles,id = id)

    article.delete()

    messages.success(request,"Makale Başarıyla Silindi")

    return redirect("Article:dashboard")
#---------------------------------------------------------------------------------------------------------#
@login_required(login_url = "user:login")
def addComment(request,id):
  
    article = get_object_or_404(Articles,id = id)

    if request.method == "POST":
        comment_author = request.user
        comment_content = request.POST.get("comment_content")
        newComment = Comments(comment_author = comment_author , comment_content = comment_content)
        
        newComment.article = article
        
        newComment.save()

    return redirect("/articles/article/" + str(id))

#---------------------------------------------------------------------------------------------------------#



