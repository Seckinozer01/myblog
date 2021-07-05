from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "Article"

urlpatterns = [
    path('',views.articles,name = "articles"),
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('addarticle/',views.addArticle,name = "addarticle"),
    path('article/<int:id>/',views.detail,name = "detail"),
    path('update/<int:id>/',views.updateArticle,name = "update"),
    path('delete/<int:id>/',views.deleteArticle,name = "delete"),
    path('comment/<int:id>/',views.addComment,name = "comment"),
    path('category/',views.categorydetail,name = "category"),
    
    
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)