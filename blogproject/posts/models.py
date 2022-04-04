from distutils.command.upload import upload
from turtle import tiltangle
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnail/', default='default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField()
    
    
    def __str__(self):
        return f"<Post {self.title}>"