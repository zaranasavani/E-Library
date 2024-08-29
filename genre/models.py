from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models(tables to store data come from user) here.


class Collection(models.Model):
    collection_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    colcover = models.CharField(max_length=1000)

    def __str__(self):
        return self.collection_name

class Piece(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    piece_type = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    year = models.IntegerField()
    piececover = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000,blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    publisher = models.CharField(max_length=200, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
