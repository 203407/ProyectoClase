from distutils.command.upload import upload
from django.db import models
from django.utils import timezone


# Create your models here.

class ImgTableModel(models.Model):
    name_img = models.CharField(max_length=255, null=True)    
    format_img = models.CharField(max_length=40,null=True)
    created = models.DateTimeField(default=timezone.now)
    edit = models.DateTimeField(blank=True, null=True, default=None)
    url_img = models.ImageField(upload_to='img/', null=False)

    class Meta:
        db_table = 'imgTable'