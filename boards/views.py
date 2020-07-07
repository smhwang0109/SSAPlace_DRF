from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .models import Tag, SSAFYArticle, SSAFYArticleComment, SSAFYArticleLike, SSAFYArticleTag, FreeArticle, FreeArticleComment, FreeArticleLike, FreeArticleTag, CodeArticle, CodeArticleComment, CodeArticleLike, CodeArticleTag
from .serializers import TagListSerializer, SSAFYArticleListSerializer, SSAFYArticleDetailSerializer, SSAFYArticleCommentSerializer, FreeArticleListSerializer, FreeArticleDetailSerializer, FreeArticleCommentSerializer, CodeArticleListSerializer, CodeArticleDetailSerializer, CodeArticleCommentSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

def get_article(model, article_id):
    return get_object_or_404(model, id=article_id)

def get_comment(model, comment_id):
    return get_object_or_404(model, id=comment_id)

def select_board(board_name):
    if board_name == 'ssafy':
        return {
            'board_model': SSAFYArticle,
            'board_comment_model': SSAFYArticleComment,
            'board_like_model': SSAFYArticleLike,
            'board_tag_model': SSAFYArticleTag,
            'board_list_serializer': SSAFYArticleListSerializer,
            'board_detail_serializer': SSAFYArticleDetailSerializer,
            'board_comment_serializer': SSAFYArticleCommentSerializer
            }
    elif board_name == 'free':
        return {
            'board_model': FreeArticle,
            'board_comment_model': FreeArticleComment,
            'board_like_model': FreeArticleLike,
            'board_tag_model': FreeArticleTag,
            'board_list_serializer': FreeArticleListSerializer,
            'board_detail_serializer': FreeArticleDetailSerializer,
            'board_comment_serializer': FreeArticleCommentSerializer
            }
    elif board_name == 'code':
        return {
            'board_model': CodeArticle,
            'board_comment_model': CodeArticleComment,
            'board_like_model': CodeArticleLike,
            'board_tag_model': CodeArticleTag,
            'board_list_serializer': CodeArticleListSerializer,
            'board_detail_serializer': CodeArticleDetailSerializer,
            'board_comment_serializer': CodeArticleCommentSerializer
            }

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
        R = select_board(board_name)
        articles = R['board_model'].objects.order_by('-created_at')
        serializer = R['board_list_serializer'](articles, many=True)
        return Response(serializer.data)
    
    # ArticleCreate
    def post(self, request, board_name):
        R = select_board(board_name)
        serializer = R['board_detail_serializer'](data=request.data['body'])
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            article = get_object_or_404(R['board_model'], id=serializer.data['id'])
            for tag_name in request.data['tags']:
                try:
                    tag = Tag.objects.get(name=tag_name)
                except:
                    tag = Tag(name=tag_name)
                    tag.save()
                R['board_tag_model'](tag=tag, article=article).save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ArticleDetailView(APIView):
    # ArticleDetail
    def get(self, request, board_name, article_id):
        R = select_board(board_name)
        article = get_article(R['board_model'], article_id)
        article.hit += 1
        article.save()
        serializer = R['board_detail_serializer'](article)
        return Response(serializer.data)

    # ArticleUpdate
    def put(self, request, board_name, article_id):
        R = select_board(board_name)
        article = get_article(R['board_model'], article_id)
        article.tags.clear()
        serializer = R['board_detail_serializer'](article, data=request.data['body'])
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            for tag_name in request.data['tags']:
                try:
                    tag = Tag.objects.get(name=tag_name)
                except:
                    tag = Tag(name=tag_name)
                    tag.save()
                R['board_tag_model'](tag=tag, article=article).save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # ArticleDelete
    def delete(self, request, board_name, article_id):
        R = select_board(board_name)
        article = get_article(R['board_model'], article_id)
        article.delete()
        return Response()

class ArticleCommentListView(APIView):
    # ArticleCommentList
    def get(self, request, board_name, article_id):
        R = select_board(board_name)
        article = get_article(R['board_model'], article_id)
        serializer = R['board_comment_serializer'](article.comments, many=True)
        return Response(serializer.data)

    # ArticleCommentCreate
    def post(self, request, board_name, article_id):
        R = select_board(board_name)
        article = get_article(R['board_model'], article_id)
        serializer = R['board_comment_serializer'](data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, article=article)
            return Response(serializer.data)
        return Response(serializer.errors)

class ArticleCommentDetailView(APIView):
    # ArticleCommentUpdate
    def put(self, request, board_name, article_id, comment_id):
        R = select_board(board_name)
        comment = get_comment(R['board_comment_model'], comment_id)
        serializer = R['board_comment_serializer'](comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # ArticleCommentDelete
    def delete(self, request, board_name, article_id, comment_id):
        R = select_board(board_name)
        comment = get_comment(R['board_comment_model'], comment_id)
        comment.delete()
        return Response()

class ArticleLikeView(APIView):
    # ArticleLike
    def post(self, request, board_name, article_id):
        R = select_board(board_name)
        article = get_article(R['board_model'], article_id)
        if article.like_users.filter(id=request.user.id).exists():
            articlelike = get_object_or_404(R['board_like_model'], user=request.user, article=article)
            articlelike.delete()
        else:
            R['board_like_model'](user=request.user, article=article).save()
        return Response()

class ArticleSearchView(APIView):
    def get(self, request, board_name, keyword):
        R = select_board(board_name)
        searched_by_title = R['board_model'].objects.filter(title__icontains=keyword)
        searched_by_content = R['board_model'].objects.filter(content__icontains=keyword)
        searched_by_tag = R['board_model'].objects.none()
        if board_name == 'ssafy':
            for tag in Tag.objects.filter(name__icontains=keyword):
                searched_by_tag = searched_by_tag.union(tag.ssafy_articles.all())
        elif board_name == 'free':
            for tag in Tag.objects.filter(name__icontains=keyword):
                searched_by_tag = searched_by_tag.union(tag.free_articles.all())

        searched_articles = searched_by_title.union(searched_by_content).union(searched_by_tag).order_by('-created_at')
        serializer = R['board_list_serializer'](searched_articles, many=True)
        return Response(serializer.data)