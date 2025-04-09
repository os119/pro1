from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)

