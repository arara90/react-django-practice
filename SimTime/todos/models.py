from django.db import models

# Create your models here.


class Todos(models.Model):
    contents = models.TextField()
    etc = models.TextField(default='hi')
