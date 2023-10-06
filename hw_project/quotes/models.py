from django.db import models
from django.contrib.auth.models import User

class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    tags = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
