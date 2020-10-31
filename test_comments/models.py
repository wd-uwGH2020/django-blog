from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    title = models.CharField(max_length=128)
    comment = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title