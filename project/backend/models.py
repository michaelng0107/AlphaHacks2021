from django.db import models

# Create your models here.

class List(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='lists', on_delete=models.CASCADE)

    def __str__(self):
        tasks = [str(task) for task in self.tasks]
        tasks_str = '\n'
        tasks_str.join(tasks)
        return f'{self.name}. Created by {self.owner.first_name}. \n {tasks_str}'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Task(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField()
    listt = models.ForeignKey('List', related_name='tasks', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('Category', related_name='category', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f'Task: {self.name}'



