from django.db import models
from django.conf import settings

from datetime import datetime
from pytz import utc

### Tag
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)


### 싸피 게시판
class SsafyArticle(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hit = models.IntegerField(default=0) # 조회수
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ssafy_articles')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='ssafy_like_articles', through='SsafyArticleLike')
    tags = models.ManyToManyField(Tag, related_name='ssafy_articles', through='SsafyArticleTag')
    
    @property
    def popularity(self):
        now = datetime.utcnow()
        during_time = (utc.localize(now) - self.created_at).total_seconds() + 3600
        return (self.like_users.count() + 1) / during_time

class SsafyArticleLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(SsafyArticle, on_delete=models.CASCADE)

class SsafyArticleComment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ssafy_comments')
    article = models.ForeignKey(SsafyArticle, on_delete=models.CASCADE, related_name='comments')

class SsafyArticleTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(SsafyArticle, on_delete=models.CASCADE)


### 자유 게시판
class FreeArticle(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hit = models.IntegerField(default=0) # 조회수
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='free_articles')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='free_like_articles', through='FreeArticleLike')
    tags = models.ManyToManyField(Tag, related_name='free_articles', through='FreeArticleTag')

    @property
    def popularity(self):
        now = datetime.utcnow()
        during_time = (utc.localize(now) - self.created_at).total_seconds() + 3600
        return (self.like_users.count() + 1) / during_time

class FreeArticleLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(FreeArticle, on_delete=models.CASCADE)

class FreeArticleComment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='free_comments')
    article = models.ForeignKey(FreeArticle, on_delete=models.CASCADE, related_name='comments')

class FreeArticleTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(FreeArticle, on_delete=models.CASCADE)