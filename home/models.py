from django.db import models

# Create your models here.


class homePageModel(models.Model):
    home_slider_image = models.ImageField(
        upload_to="homeSliderImage/", max_length=250, null=True, default=None)
    home_slider_image_alt_text = models.CharField(max_length=250)
    home_slider_image_href = models.CharField(max_length=1000)
