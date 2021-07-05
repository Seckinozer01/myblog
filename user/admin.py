from django.contrib import admin

from .models import Hesap


# Register your models here.
@admin.register(Hesap)
class ArticleAdmin(admin.ModelAdmin):
    list_display =["email","username","register_date","last_login",]
    list_display_links = ["email","username"]
    search_fields=["email"]
    list_filter = ["register_date"]
    class Meta:
        model = Hesap