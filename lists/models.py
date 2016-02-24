from django.db import models

# Create your models here.

class Item(models.Model):
    text = models.TextField(default='')

class test(models.Model):
    test1 = models.CharField(max_length=100)