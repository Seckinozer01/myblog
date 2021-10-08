from django.contrib import admin
from .models import Articles,Comments,Category
# Register your models here.

admin.site.register(Comments)

admin.site.register(Category)






@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display =["title","author","created_date","article_image","category",]
    list_display_links = ["title","created_date"]
    search_fields=["title"]
    list_filter = ["created_date"]
    class Meta:
        model = Articles