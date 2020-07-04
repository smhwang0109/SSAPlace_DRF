from django.core import serializers as django_serializers

from rest_framework import serializers
from .models import SsafyArticle, SsafyArticleComment, FreeArticle, FreeArticleComment
from accounts.serializers import UserSerializer

### SSAFY 게시판

class SsafyArticleListSerializer(serializers.ModelSerializer):    
    author = UserSerializer(required=False)
    class Meta:
        model = SsafyArticle
        fields = ['id', 'title', 'hit', 'author']

class SsafyArticleCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    # article = SsafyArticleDetailSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    class Meta:
        model = SsafyArticleComment
        # fields = '__all__'
        fields = ('content','author','id','created_at','updated_at')
    

class SsafyArticleDetailSerializer(serializers.ModelSerializer):    
    author = UserSerializer(required=False)
    # ssafy_comments = serializers.SerializerMethodField()
    ssafy_comments = SsafyArticleCommentSerializer(required=False, many=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    class Meta:
        model = SsafyArticle
        fields = '__all__'
        read_only_fields = ['hit']

class SsafyArticleCommentListSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
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
    class Meta:
        model = FreeArticle
        fields = ['id', 'title', 'hit', 'author']

class FreeArticleCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    # article = FreeArticleDetailSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    class Meta:
        model = FreeArticleComment
        fields = '__all__'
    

class FreeArticleDetailSerializer(serializers.ModelSerializer):    
    author = UserSerializer(required=False)
    free_comments = FreeArticleCommentSerializer(required=False, many=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    class Meta:
        model = FreeArticle
        fields = '__all__'
        read_only_fields = ['hit']

class FreeArticleCommentListSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    class Meta:
        model = FreeArticleComment
        fields = '__all__'

class FreeArticleCommentDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    article = FreeArticleDetailSerializer(required=False)
    class Meta:
        model = FreeArticleComment
        fields = '__all__'
