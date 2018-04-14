from django.db import models
from django.contrib.auth.models import User


class Feed(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    post = models.TextField(max_length=255,blank=False)
    likes = models.IntegerField(default=0)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=500,blank=True)
    telegram_id = models.CharField(max_length=50,blank=True)
    birth_date = models.DateField(null=True,blank=True)
    picture = models.ImageField(blank=True,upload_to='pics/',)