# Generated by Django 4.0.4 on 2022-04-15 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourapp', '0006_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/images'),
        ),
    ]
