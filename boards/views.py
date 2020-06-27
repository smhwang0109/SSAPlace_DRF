from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .models import Board, Article, ArticleLike, ArticleComment
from .serializers import ArticleSerializer, ArticleCommentSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

def get_article(article_id):
    return get_object_or_404(Article, id=article_id)

def get_comment(comment_id):
    return get_object_or_404(ArticleComment, id=comment_id)

class ArticleListView(APIView):
    # ArticleList
    def get(self, request, board_id):

        if board_id == 0: # 전체 게시물(0)
            articles = Article.objects.order_by('-created_at')
        elif board_id == 10000: # 인기 게시물(10000)
            articles = Article.objects.all()
            articles = sorted(articles, key=lambda article: article.popularity, reverse=True)
        else: # 특정 게시판 게시물
            # 1 => 자유 게시판
            # 2 => 싸피 게시판
            # 3 => 취업/진로 게시판
            board = get_object_or_404(Board, id=board_id)
            articles = Article.objects.filter(board=board).order_by('-created_at')

        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    # ArticleCreate
    def post(self, request, board_id):
        board = get_object_or_404(Board, id=board_id)

        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, board=board)
            return Response(serializer.data)
        return Response(serializer.errors)

class ArticleDetailView(APIView):
    # ArticleDetail
    def get(self, request, article_id):
        article = get_article(article_id)
        article.hit += 1
        article.save()
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # ArticleUpdate
    def put(self, request, article_id):
        article = get_article(article_id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # ArticleDelete
    def delete(self, request, article_id):
        article = self.get_article(article_id)
        article.delete()
        return Response()

########################

class ArticleCommentListView(APIView):
    # CommentCreate
    def post(self, request, article_id):
        article = get_article(article_id)
        serializer = ArticleCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, article=article)
            return Response(serializer.data)
        return Response(serializer.errors)

class ArticleCommentDetailView(APIView):
    # CommentUpdate
    def put(self, request, article_id, comment_id):
        comment = get_comment(comment_id)
        serializer = ArticleCommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # CommentDelete
    def delete(self, request, article_id, comment_id):
        comment = get_comment(comment_id)
        comment.delete()
        return Response()

########################

class ArticleLikeView(APIView):
    # Like
    def post(self, request, article_id):
        article = get_article(article_id)
        if article.like_users.filter(id=request.user.id).exists():
            articlelike = get_object_or_404(ArticleLike, user=request.user, article=article)
            articlelike.delete()
        else:
            articlelike = ArticleLike()
            articlelike.user = request.user
            articlelike.article = article
            articlelike.save()
        return Response()

########################

class ArticleSearchView(APIView):
    def get(self, request, keyword):
        searched_by_title = Article.objects.filter(title__icontains=keyword)
        searched_by_content = Article.objects.filter(content__icontains=keyword)
        searched_articles = searched_by_title.union(searched_by_content).order_by('-created_at')
        serializer = ArticleSerializer(searched_articles, many=True)
        return Response(serializer.data)