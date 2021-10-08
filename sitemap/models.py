from django.db import models
from myblog.settings import  AUTH_USER_MODEL

from ckeditor.fields import RichTextField
# Create your models here.
class SupportMessage(models.Model):
    
    support_name = models.CharField(max_length = 50,verbose_name = "İsim Soyisim")
    support_email = models.EmailField(max_length = 50,verbose_name = "Mail Adresi")
    support_phone = models.CharField(max_length = 50,verbose_name = "Telefon Numarası")
    support_content = models.CharField(max_length = 50,verbose_name = "Başlık")
    support_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.support_content
    class Meta:
        ordering = ['-support_date']
        