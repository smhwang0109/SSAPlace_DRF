from django.db import models
from django.conf import settings

from datetime import datetime
from pytz import utc

### Tag
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)


### 싸피 게시판
class SSAFYArticle(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hit = models.IntegerField(default=0) # 조회수
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ssafy_articles')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='ssafy_like_articles', through='SSAFYArticleLike')
    tags = models.ManyToManyField(Tag, related_name='ssafy_articles', through='SSAFYArticleTag')
    
    @property
    def popularity(self):
        now = datetime.utcnow()
        during_time = (utc.localize(now) - self.created_at).total_seconds() + 3600
        return (self.like_users.count() + 1) / during_time

class SSAFYArticleLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(SSAFYArticle, on_delete=models.CASCADE)

class SSAFYArticleComment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ssafy_comments')
    article = models.ForeignKey(SSAFYArticle, on_delete=models.CASCADE, related_name='comments')

class SSAFYArticleTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(SSAFYArticle, on_delete=models.CASCADE)


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
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='free_comments')
    article = models.ForeignKey(FreeArticle, on_delete=models.CASCADE, related_name='comments')

class FreeArticleTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(FreeArticle, on_delete=models.CASCADE)


### 코드 게시판
class CodeArticle(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hit = models.IntegerField(default=0) # 조회수
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='code_articles')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='code_like_articles', through='CodeArticleLike')
    tags = models.ManyToManyField(Tag, related_name='code_articles', through='CodeArticleTag')

    @property
    def popularity(self):
        now = datetime.utcnow()
        during_time = (utc.localize(now) - self.created_at).total_seconds() + 3600
        return (self.like_users.count() + 1) / during_time

class CodeArticleLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(CodeArticle, on_delete=models.CASCADE)

class CodeArticleComment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='code_comments')
    article = models.ForeignKey(CodeArticle, on_delete=models.CASCADE, related_name='comments')

class CodeArticleTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(CodeArticle, on_delete=models.CASCADE)