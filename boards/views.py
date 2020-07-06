from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .models import SsafyArticle, SsafyArticleComment, SsafyArticleLike, FreeArticle, FreeArticleComment, FreeArticleLike, Tag, SsafyArticleTag, FreeArticleTag
from .serializers import SsafyArticleListSerializer, SsafyArticleDetailSerializer, SsafyArticleCommentSerializer, FreeArticleListSerializer, FreeArticleDetailSerializer, FreeArticleCommentSerializer, TagListSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

def get_article(model, article_id):
    return get_object_or_404(model, id=article_id)

def get_comment(model, comment_id):
    return get_object_or_404(model, id=comment_id)

### Tags
class TagListView(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        data = []
        for tag in tags:
            data.append(tag.name)
        return Response(data)


### Boards
class ArticleListView(APIView):
    # ArticleList
    def get(self, request, board_name):
        if board_name == 'ssafy': # 싸피게시판
            board_model = SsafyArticle
            board_serializer = SsafyArticleListSerializer
        elif board_name == 'free': # 자유게시판
            board_model = FreeArticle
            board_serializer = FreeArticleListSerializer

        articles = board_model.objects.order_by('-created_at')
        serializer = board_serializer(articles, many=True)
        return Response(serializer.data)
    
    # ArticleCreate
    def post(self, request, board_name):
        if board_name == 'ssafy': # 싸피게시판
            board_model = SsafyArticle
            board_serializer = SsafyArticleDetailSerializer
            board_tag_model = SsafyArticleTag
        elif board_name == 'free': # 자유게시판
            board_model = FreeArticle
            board_serializer = FreeArticleDetailSerializer
            board_tag_model = FreeArticleTag

        serializer = board_serializer(data=request.data['body'])
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            article = get_object_or_404(board_model, id=serializer.data['id'])
            for tag_name in request.data['tags']:
                try:
                    tag = Tag.objects.get(name=tag_name)
                except:
                    tag = Tag(name=tag_name)
                    tag.save()
                board_tag_model(tag=tag, article=article).save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ArticleDetailView(APIView):
    # ArticleDetail
    def get(self, request, board_name, article_id):
        if board_name == 'ssafy': # 싸피게시판
            board_model = SsafyArticle
            board_serializer = SsafyArticleDetailSerializer
        elif board_name == 'free': # 자유게시판
            board_model = FreeArticle
            board_serializer = FreeArticleDetailSerializer

        article = get_article(board_model, article_id)
        article.hit += 1
        article.save()
        serializer = board_serializer(article)
        return Response(serializer.data)

    # ArticleUpdate
    def put(self, request, board_name, article_id):
        if board_name == 'ssafy': # 싸피게시판
            board_model = SsafyArticle
            board_serializer = SsafyArticleDetailSerializer
            board_tag_model = SsafyArticleTag
        elif board_name == 'free': # 자유게시판
            board_model = FreeArticle
            board_serializer = FreeArticleDetailSerializer
            board_tag_model = FreeArticleTag

        article = get_article(board_model, article_id)
        article.tags.clear()

        serializer = board_serializer(article, data=request.data['body'])
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            for tag_name in request.data['tags']:
                try:
                    tag = Tag.objects.get(name=tag_name)
                except:
                    tag = Tag(name=tag_name)
                    tag.save()
                board_tag_model(tag=tag, article=article).save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # ArticleDelete
    def delete(self, request, board_name, article_id):
        if board_name == 'ssafy': # 싸피게시판
            board_model = SsafyArticle
        elif board_name == 'free': # 자유게시판
            board_model = FreeArticle
        article = get_article(board_model, article_id)
        article.delete()
        return Response()

class ArticleCommentListView(APIView):
    # ArticleCommentList
    def get(self, request, board_name, article_id):
        if board_name == 'ssafy': # 싸피게시판
            board_model = SsafyArticle
            board_serializer = SsafyArticleCommentSerializer
        elif board_name == 'free': # 자유게시판
            board_model = FreeArticle
            board_serializer = FreeArticleCommentSerializer

        article = get_article(board_model, article_id)
        serializer = board_serializer(article.comments, many=True)
        return Response(serializer.data)

    # ArticleCommentCreate
    def post(self, request, board_name, article_id):
        if board_name == 'ssafy': # 싸피게시판
            board_model = SsafyArticle
            board_serializer = SsafyArticleCommentSerializer
        elif board_name == 'free': # 자유게시판
            board_model = FreeArticle
            board_serializer = FreeArticleCommentSerializer

        article = get_article(board_model, article_id)
        serializer = board_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, article=article)
            return Response(serializer.data)
        return Response(serializer.errors)

class ArticleCommentDetailView(APIView):
    # ArticleCommentUpdate
    def put(self, request, board_name, article_id, comment_id):
        if board_name == 'ssafy': # 싸피게시판
            board_model = SsafyArticleComment
            board_serializer = SsafyArticleCommentSerializer
        elif board_name == 'free': # 자유게시판
            board_model = FreeArticleComment
            board_serializer = FreeArticleCommentSerializer

        comment = get_comment(board_model, comment_id)
        serializer = board_serializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # ArticleCommentDelete
    def delete(self, request, board_name, article_id, comment_id):
        if board_name == 'ssafy': # 싸피게시판
            board_model = SsafyArticleComment
        elif board_name == 'free': # 자유게시판
            board_model = FreeArticleComment

        comment = get_comment(board_model, comment_id)
        comment.delete()
        return Response()

class ArticleLikeView(APIView):
    # ArticleLike
    def post(self, request, board_name, article_id):
        if board_name == 'ssafy': # 싸피게시판
            board_model = SsafyArticle
            board_like_model = SsafyArticleLike
        elif board_name == 'free': # 자유게시판
            board_model = FreeArticle
            board_like_model = FreeArticleLike

        article = get_article(board_model, article_id)
        if article.like_users.filter(id=request.user.id).exists():
            articlelike = get_object_or_404(board_like_model, user=request.user, article=article)
            articlelike.delete()
        else:
            board_like_model(user=request.user, article=article).save()
        return Response()

class ArticleSearchView(APIView):
    def get(self, request, board_name, keyword):
        if board_name == 'ssafy': # 싸피게시판
            board_model = SsafyArticle
            board_serializer = SsafyArticleListSerializer
        elif board_name == 'free': # 자유게시판
            board_model = FreeArticle
            board_serializer = FreeArticleListSerializer

        searched_by_title = board_model.objects.filter(title__icontains=keyword)
        searched_by_content = board_model.objects.filter(content__icontains=keyword)
        searched_by_tag = board_model.objects.none()
        if board_name == 'ssafy':
            for tag in Tag.objects.filter(name__icontains=keyword):
                searched_by_tag = searched_by_tag.union(tag.ssafy_articles.all())
        elif board_name == 'free':
            for tag in Tag.objects.filter(name__icontains=keyword):
                searched_by_tag = searched_by_tag.union(tag.free_articles.all())

        searched_articles = searched_by_title.union(searched_by_content).union(searched_by_tag).order_by('-created_at')
        serializer = board_serializer(searched_articles, many=True)
        return Response(serializer.data)