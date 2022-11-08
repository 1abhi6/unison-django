from django.contrib import admin
from news.models import News

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'news_desc','news_image','new_img_alt_text')

admin.site.register(News,NewsAdmin)
