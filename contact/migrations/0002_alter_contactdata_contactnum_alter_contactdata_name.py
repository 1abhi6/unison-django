# Generated by Django 4.1.2 on 2022-11-06 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdata',
            name='contactNum',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]