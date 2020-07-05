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
    class Meta:
        model = SsafyArticle
        fields = ['id', 'title', 'hit', 'author', 'created_at']

class SsafyArticleDetailSerializer(serializers.ModelSerializer):    
    author = UserSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    class Meta:
        model = SsafyArticle
        fields = '__all__'
        read_only_fields = ['hit']

class SsafyArticleCommentListSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    class Meta:
        model = SsafyArticleComment
        fields = '__all__'

class SsafyArticleCommentDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    article = SsafyArticleDetailSerializer(required=False)
    class Meta:
        model = SsafyArticleComment
        fields = '__all__'
    

### 자유 게시판

class FreeArticleListSerializer(serializers.ModelSerializer):    
    author = UserSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d", required=False)
    class Meta:
        model = FreeArticle
        fields = ['id', 'title', 'hit', 'author', 'created_at']

class FreeArticleDetailSerializer(serializers.ModelSerializer):    
    author = UserSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    class Meta:
        model = FreeArticle
        fields = '__all__'
        read_only_fields = ['hit']

class FreeArticleCommentListSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    class Meta:
        model = FreeArticleComment
        fields = '__all__'

class FreeArticleCommentDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    article = FreeArticleDetailSerializer(required=False)
    class Meta:
        model = FreeArticleComment
        fields = '__all__'
    
