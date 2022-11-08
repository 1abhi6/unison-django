from django.db import models

# Create your models here.


class About(models.Model):
    aboutImg = models.CharField(max_length=50)
    aboutDesc = models.TextField()
