from django.db import models
from django.conf import settings

from datetime import datetime
from pytz import utc

class Board(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    # 1 => 자유 게시판
    # 2 => 싸피 게시판
    # 3 => 취업/진로 게시판

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hit = models.IntegerField(default=0) # 조회수
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    board = models.ForeignKey(Board, on_delete=models.SET_DEFAULT, default=1, related_name='articles') # default => 자유 게시판
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', through='ArticleLike')

    @property
    def popularity(self):
        now = datetime.utcnow()
        during_time = (utc.localize(now) - self.created_at).total_seconds() + 3600
        return (self.like_users.count() + 1) / during_time

class ArticleLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

class ArticleComment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')