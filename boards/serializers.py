from django.core import serializers as django_serializers

from rest_framework import serializers
from .models import SsafyArticle, SsafyArticleComment, FreeArticle, FreeArticleComment, Tag
from accounts.serializers import UserSerializer

### Tags
class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

### SSAFY 게시판
class SsafyArticleListSerializer(serializers.ModelSerializer):    
    author = UserSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d", required=False)
    tags = TagListSerializer(required=False, many=True)
    class Meta:
        model = SsafyArticle
        fields = ['id', 'title', 'hit', 'author', 'created_at', 'updated_at', 'tags', 'like_users']

class SsafyArticleCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    article = SsafyArticleListSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    class Meta:
        model = SsafyArticleComment
        fields = '__all__'

class SsafyArticleDetailSerializer(serializers.ModelSerializer):    
    author = UserSerializer(required=False)
    comments = SsafyArticleCommentSerializer(required=False, many=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    tags = TagListSerializer(required=False, many=True)
    class Meta:
        model = SsafyArticle
        fields = '__all__'
        read_only_fields = ['hit']

    

### 자유 게시판
class FreeArticleListSerializer(serializers.ModelSerializer):    
    author = UserSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d", required=False)
    tags = TagListSerializer(required=False, many=True)
    class Meta:
        model = FreeArticle
        fields = ['id', 'title', 'hit', 'author', 'created_at', 'updated_at', 'tags', 'like_users']

class FreeArticleCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    article = FreeArticleListSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    class Meta:
        model = FreeArticleComment
        fields = '__all__'

class FreeArticleDetailSerializer(serializers.ModelSerializer):    
    author = UserSerializer(required=False)
    comments = FreeArticleCommentSerializer(required=False, many=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    like_users = UserSerializer(required=False, many=True)
    tags = TagListSerializer(required=False, many=True)
    class Meta:
        model = FreeArticle
        fields = '__all__'
        read_only_fields = ['hit']