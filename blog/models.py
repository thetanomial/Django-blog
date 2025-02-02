from django.db import models

# Create your models here.
from django.conf import settings 
class BlogPost(models.Model):

    title = models.CharField(max_length=200,blank=False)
    description = models.TextField(blank=False)

    published_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


