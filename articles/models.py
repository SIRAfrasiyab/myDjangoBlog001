from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + " ..."