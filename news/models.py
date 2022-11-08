from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.


class News(models.Model):
    news_title = models.CharField(max_length=50)
    news_desc = HTMLField()
    # For file uploading use FileFeild()
    news_image = models.FileField(
        upload_to='news/', max_length=250, null=True, default=None)
    new_img_alt_text = models.TextField(
        max_length=50, null=True, default="unison")
    # To generate slug field based on news_title, it will be unique, can be null and by default it do not have any value
    news_title_slug = AutoSlugField(
        populate_from='news_title', unique=True, null=True, default=None)
