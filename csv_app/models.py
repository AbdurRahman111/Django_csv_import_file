from django.db import models

# Create your models here.

class name_database(models.Model):
    name = models.CharField(max_length=20)
    add = models.CharField(max_length=20)
