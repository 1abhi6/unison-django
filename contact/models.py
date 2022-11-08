from django.db import models

# Create your models here.


class contactData(models.Model):
    name = models.CharField(max_length=50, null=True)
    contactNum = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)
