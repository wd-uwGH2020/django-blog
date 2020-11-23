from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, related_name="Categories")

    def __str__(self):
        return self.name

    # in our Post model, we used a ForeignKeyField field to match an author to her posts. This models the situation in which a single author can have many posts, while each post has only one author. We call this a Many to One relationship. But any given Post might belong in more than one Category. And it would be a waste to allow only one Post for each Category. This is why we used the ManyToManyField

    class Meta:
        verbose_name_plural = "Categories"
