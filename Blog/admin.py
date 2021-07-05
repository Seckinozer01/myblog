from django.contrib import admin
from .models import ShowArticle,AddComment,SendSupport ,Category
# Register your models here.

admin.site.register(AddComment)

admin.site.register(SendSupport)
admin.site.register(Category)






@admin.register(ShowArticle)
class ArticleAdmin(admin.ModelAdmin):
    list_display =["title","author","created_date","article_image","category",]
    list_display_links = ["title","created_date"]
    search_fields=["title"]
    list_filter = ["created_date"]
    class Meta:
        model = ShowArticle