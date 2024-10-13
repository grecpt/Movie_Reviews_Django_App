from django.db import models

# Create your models here.
from django.shortcuts import render

class News(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()
    