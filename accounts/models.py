from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=50, null=True)
    self_introduction = models.CharField(null=True, max_length = 500)
    location = models.CharField(null=True, max_length = 100)
    email = models.EmailField(null=True)
    instagram = models.URLField(null=True)
    github = models.URLField(null=True) 
    facebook = models.URLField(null=True)
    homepage =  models.URLField(null=True)
    linkedin =  models.URLField(null=True) 
    # 주 사용 언어/프레임워크
    # front_language = models.ManyToManyField(UseLanguage, related_name='front_languages', through='FrontUse')
    # back_language = models.ManyToManyField(UseLanguage, related_name='back_languages', through='BackUse')

class Interest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    interest = models.CharField(max_length=30)

class Languages(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    language = models.CharField(max_length=20)
