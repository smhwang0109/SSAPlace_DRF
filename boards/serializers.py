from django.core import serializers as django_serializers

from rest_framework import serializers
from .models import Tag, SSAFYArticle, SSAFYArticleComment, FreeArticle, FreeArticleComment, CodeArticle, CodeArticleComment
from accounts.serializers import UserSerializer

### Tag
class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


### 싸피 게시판
class SSAFYArticleListSerializer(serializers.ModelSerializer):    
    author = UserSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d", required=False)
    tags = TagListSerializer(required=False, many=True)
    class Meta:
        model = SSAFYArticle
        fields = ['id', 'title', 'hit', 'author', 'created_at', 'tags', 'like_users']

class SSAFYArticleCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    article = SSAFYArticleListSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    class Meta:
        model = SSAFYArticleComment
        fields = '__all__'

class SSAFYArticleDetailSerializer(serializers.ModelSerializer):    
    author = UserSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    comments = SSAFYArticleCommentSerializer(required=False, many=True)
    tags = TagListSerializer(required=False, many=True)
    class Meta:
        model = SSAFYArticle
        fields = '__all__'
        read_only_fields = ['hit']


### 자유 게시판
class FreeArticleListSerializer(serializers.ModelSerializer):    
    author = UserSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d", required=False)
    tags = TagListSerializer(required=False, many=True)
    class Meta:
        model = FreeArticle
        fields = ['id', 'title', 'hit', 'author', 'created_at', 'tags', 'like_users']

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
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    comments = FreeArticleCommentSerializer(required=False, many=True)
    tags = TagListSerializer(required=False, many=True)
    class Meta:
        model = FreeArticle
        fields = '__all__'
        read_only_fields = ['hit']


### 코드 게시판
class CodeArticleListSerializer(serializers.ModelSerializer):    
    author = UserSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d", required=False)
    tags = TagListSerializer(required=False, many=True)
    class Meta:
        model = CodeArticle
        fields = ['id', 'title', 'hit', 'author', 'created_at', 'tags', 'like_users']

class CodeArticleCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    article = CodeArticleListSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    class Meta:
        model = CodeArticleComment
        fields = '__all__'

class CodeArticleDetailSerializer(serializers.ModelSerializer):    
    author = UserSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    comments = CodeArticleCommentSerializer(required=False, many=True)
    tags = TagListSerializer(required=False, many=True)
    class Meta:
        model = CodeArticle
        fields = '__all__'
        read_only_fields = ['hit']