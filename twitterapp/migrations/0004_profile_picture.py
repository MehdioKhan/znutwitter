# Generated by Django 2.0.3 on 2018-04-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterapp', '0003_profile_telegram_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
