# Generated by Django 4.2.4 on 2023-08-05 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(upload_to='blog_images/'),
        ),
    ]
