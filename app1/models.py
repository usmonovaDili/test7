from django.db import models


# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    auther = models.CharField(max_length=40)

    def __str__(self):
        return self.title
