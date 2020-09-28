from django.db import models

class Todo(models.Model):
    titke = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    done = models.DateField(blank=False, null=True)
