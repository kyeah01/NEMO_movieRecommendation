# Generated by Django 2.2.4 on 2019-09-30 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_profile_photo_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='photo_url',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]