from django.core import serializers as django_serializers

from rest_framework import serializers
from .models import SsafyArticle, SsafyArticleComment, FreeArticle, FreeArticleComment
from accounts.serializers import UserSerializer

### SSAFY 게시판

class SsafyArticleListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = SsafyArticle
        fields = ['title', 'hit', 'author']

class SsafyArticleDetailSerializer(serializers.ModelSerializer):    
    class Meta:
        model = SsafyArticle
        fields = '__all__'
        read_only_fields = ['hit']

    author = UserSerializer(required=False)
    ssafy_comments = serializers.SerializerMethodField()

    def get_ssafy_comments(self, obj):
        return django_serializers.serialize('json', obj.ssafy_comments.order_by('-created_at'), ensure_ascii=False)

class SsafyArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SsafyArticleComment
        fields = '__all__'
    
    author = UserSerializer(required=False)
    article = SsafyArticleDetailSerializer(required=False)

### 자유 게시판

class FreeArticleListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = FreeArticle
        fields = ['title', 'hit', 'author']

class FreeArticleDetailSerializer(serializers.ModelSerializer):    
    class Meta:
        model = FreeArticle
        fields = '__all__'
        read_only_fields = ['hit']

    author = UserSerializer(required=False)
    free_comments = serializers.SerializerMethodField()

    def get_free_comments(self, obj):
        return django_serializers.serialize('json', obj.free_comments.order_by('-created_at'), ensure_ascii=False)

class FreeArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeArticleComment
        fields = '__all__'
    
    author = UserSerializer(required=False)
    article = FreeArticleDetailSerializer(required=False)
