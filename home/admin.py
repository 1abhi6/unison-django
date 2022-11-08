from django.contrib import admin
from home.models import homePageModel

# Register your models here.
class HomePageAdmin(admin.ModelAdmin):
    list_display=['home_slider_image','home_slider_image_alt_text','home_slider_image_href']

admin.site.register(homePageModel,HomePageAdmin)