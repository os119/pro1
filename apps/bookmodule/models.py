from django.db import models
from django.utils import timezone
# Create your models here.



class Publisher(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=300)

class Author(models.Model):
    name = models.CharField(max_length=300)

class Book(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.SmallIntegerField(default=1)
    pubdate = models.DateTimeField(default=timezone.now)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
