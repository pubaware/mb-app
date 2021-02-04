from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()
    
    def __str__(self):
        # this will display the first 50 chars
        # of the text field of each post
        return self.text[:50]


