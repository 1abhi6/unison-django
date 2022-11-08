# Generated by Django 4.1.2 on 2022-11-06 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='homePageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_slider_image', models.ImageField(default=None, max_length=250, null=True, upload_to='homeSliderImage/')),
                ('home_slider_image_alt_text', models.CharField(max_length=250)),
                ('home_slider_image_href', models.CharField(max_length=1000)),
            ],
        ),
    ]