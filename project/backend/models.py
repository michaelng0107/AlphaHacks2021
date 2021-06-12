from django.db import models

# Create your models here.

class List(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='lists', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=50)

class Task(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField()
    category = models.ForeignKey('Category', related_name='category', on_delete=models.CASCADE)
    description = models.TextField()


