from django.db import models
from django.utils import timezone


# Create your models here.

class PrimerModelo(models.Model):
    name_img = models.CharField(max_length=255, null=False)
    url_img = models.CharField(max_length=400, null=False)
    format_img = models.CharField(max_length=40, null=False)
    created = models.DateTimeField(default=timezone.now)
    edit = models.DateTimeField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'imgTable'