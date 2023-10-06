from django.db import models

class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    tags = models.CharField(max_length=200)
    