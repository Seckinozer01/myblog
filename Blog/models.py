from django.db import models
from ozer.settings import  AUTH_USER_MODEL

from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name="Kategori Adı")
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    def __str__(self):
        return self.name


class ShowArticle(models.Model):
    author = models.ForeignKey("user.Hesap",on_delete = models.CASCADE,verbose_name = "Yazar ")
    title = models.CharField(max_length = 200,verbose_name = "Başlık")
    category = models.ForeignKey(Category,on_delete = models.CASCADE,verbose_name = "Kategori")
    content = RichTextField(verbose_name = "İçerik")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(blank = True,null = True,verbose_name="Fotoğraf Ekleyin")
    
    
    def get_all_articles():
        return ShowArticle.objects.all()

    def get_all_articles_by_categoryid(category_id):
        if category_id:
            return ShowArticle.objects.filter(category = category_id)

        else:
            return ShowArticle.get_all_articles()
                
    @property
    def num_likes(self):
        return self.liked.all().count() 

    def __str__(self):
        return self.title

    class Meta :
        ordering = ['-created_date']



class AddComment(models.Model):
    article = models.ForeignKey(ShowArticle,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
    comment_author = models.ForeignKey("user.Hesap",on_delete = models.CASCADE,verbose_name = "Yorum Yapan")
    comment_content = models.CharField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']
 

class SendSupport(models.Model):
    support_tittle = models.CharField(max_length = 500,verbose_name = "İçerik")
    support_name = models.CharField(max_length = 50,verbose_name = "İsim Soyisim")
    support_email = models.EmailField(max_length = 50,verbose_name = "Mail Adresi")
    support_phone = models.CharField(max_length = 50,verbose_name = "Telefon Numarası")
    support_content = models.CharField(max_length = 50,verbose_name = "Başlık")
    support_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.support_content
    class Meta:
        ordering = ['-support_date']
        
    


    