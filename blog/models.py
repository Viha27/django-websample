from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.TextField()
    content = models.TextField(null=True)
    slug = models.SlugField(unique=True)
    #slug is url encoded value 


class Blog:
    title = "hello blog"
    content = "something cooool"    
