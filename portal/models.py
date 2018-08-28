from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class SandbStatic(models.Model):
    name = models.CharField(max_length=30, unique=True)
    sandb_static = HTMLField('sandb_static')

    def __str__(self):
        return self.name
