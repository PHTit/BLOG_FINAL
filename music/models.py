from django.db import models
import datetime
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.
class Music(models.Model):
    YEAR_CHOICES = []
    for r in range(1880, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    
    name = models.CharField(max_length=40, default="", verbose_name="Nombre")
    cover = models.ImageField(upload_to='staticfiles/covers/',  null=True, blank=True, verbose_name="Poster")
    singer = models.CharField(max_length=40, default="", verbose_name="Cantante")
    year = models.IntegerField(('Año'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    review = RichTextField(blank = True, null=True, verbose_name="Reseña")
    post_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,null=True,blank=True,on_delete=models.DO_NOTHING, verbose_name="Autor")


    def __str__(self):
        return f'{self.name}'
