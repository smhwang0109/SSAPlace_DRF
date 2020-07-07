from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from teams.models import Interest, UseLanguage

class User(AbstractUser):
    messages_to = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='messages_from', through='MessageGroup')

class MessageGroup(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='to_user')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='from_user')

class Message(models.Model):
    message_group = models.ForeignKey(MessageGroup, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    self_introduction = models.CharField(null=True, max_length = 500, blank=True)
    location = models.CharField(null=True, max_length = 100, blank=True)
    email = models.EmailField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True) 
    facebook = models.URLField(null=True, blank=True)
    homepage =  models.URLField(null=True, blank=True)
    linkedin =  models.URLField(null=True, blank=True)
    interests = models.ManyToManyField(Interest, related_name='users', through='ProfileInterest')
    languages = models.ManyToManyField(UseLanguage, related_name='users', through='ProfileLanguage')

class ProfileInterest(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)

class ProfileLanguage(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    language = models.ForeignKey(UseLanguage, on_delete=models.CASCADE)