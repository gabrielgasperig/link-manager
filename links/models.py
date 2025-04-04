from django.db import models

# Create your models here.

class Link(models.Model):
    url = models.URLField(unique=True)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
