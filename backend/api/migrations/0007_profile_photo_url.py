# Generated by Django 2.2.4 on 2019-09-30 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_profile_recommend_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo_url',
            field=models.TextField(default=''),
        ),
    ]