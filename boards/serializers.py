from django.core import serializers as django_serializers

from rest_framework import serializers
from .models import Board, Article, ArticleLike, ArticleComment
from accounts.serializers import UserSerializer

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['hit']

    author = UserSerializer(required=False)
    board = BoardSerializer(required=False)
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        return django_serializers.serialize('json', obj.comments.order_by('-created_at'), ensure_ascii=False)

class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = '__all__'
    
    author = UserSerializer(required=False)
    article = ArticleSerializer(required=False)
