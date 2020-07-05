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

### SSAFY 게시판
class SsafyArticleListView(APIView):
    # SSAFY ArticleList
    def get(self, request):
        articles = SsafyArticle.objects.order_by('-created_at')
        serializer = SsafyArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    # SSAFY ArticleCreate
    def post(self, request):
        serializer = SsafyArticleDetailSerializer(data=request.data['body'])
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            article = get_object_or_404(SsafyArticle, id=serializer.data['id'])
            for tag_name in request.data['tags']:
                try:
                    tag = get_object_or_404(Tag, name=tag_name)
                except:
                    tag = Tag()
                    tag.name = tag_name
                    tag.save()
                ssafyarticletag = SsafyArticleTag()
                ssafyarticletag.article = article
                ssafyarticletag.tag = tag
                ssafyarticletag.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class SsafyArticleDetailView(APIView):
    # SSAFY ArticleDetail
    def get(self, request, article_id):
        article = get_article(SsafyArticle, article_id)
        article.hit += 1
        article.save()
        serializer = SsafyArticleDetailSerializer(article)
        return Response(serializer.data)

    # SSAFY ArticleUpdate
    def put(self, request, article_id):
        article = get_article(SsafyArticle, article_id)
        for ssafyarticletag in SsafyArticleTag.objects.filter(article=article):
            ssafyarticletag.delete()

        serializer = SsafyArticleDetailSerializer(article, data=request.data['body'])
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            for tag_name in request.data['tags']:
                try:
                    tag = get_object_or_404(Tag, name=tag_name)
                except:
                    tag = Tag()
                    tag.name = tag_name
                    tag.save()
                ssafyarticletag = SsafyArticleTag()
                ssafyarticletag.article = article
                ssafyarticletag.tag = tag
                ssafyarticletag.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # SSAFY ArticleDelete
    def delete(self, request, article_id):
        article = get_article(SsafyArticle, article_id)
        article.delete()
        return Response()

class SsafyArticleCommentListView(APIView):
    # Ssafy ArticleCommentList
    def get(self, request, article_id):
        article = get_article(SsafyArticle, article_id)
        serializer = SsafyArticleCommentSerializer(article.comments, many=True)
        return Response(serializer.data)

    # Ssafy ArticleCommentCreate
    def post(self, request, article_id):
        article = get_article(SsafyArticle, article_id)
        serializer = SsafyArticleCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, article=article)
            return Response(serializer.data)
        return Response(serializer.errors)

class SsafyArticleCommentDetailView(APIView):
    # SSAFY ArticleCommentUpdate
    def put(self, request, article_id, comment_id):
        comment = get_comment(SsafyArticleComment, comment_id)
        serializer = SsafyArticleCommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # SSAFY ArticleCommentDelete
    def delete(self, request, article_id, comment_id):
        comment = get_comment(SsafyArticleComment, comment_id)
        comment.delete()
        return Response()

class SsafyArticleLikeView(APIView):
    # SSAFY ArticleLike
    def post(self, request, article_id):
        article = get_article(SsafyArticle, article_id)
        if article.like_users.filter(id=request.user.id).exists():
            articlelike = get_object_or_404(SsafyArticleLike, user=request.user, article=article)
            articlelike.delete()
        else:
            articlelike = SsafyArticleLike()
            articlelike.user = request.user
            articlelike.article = article
            articlelike.save()
        return Response()

class SsafyArticleSearchView(APIView):
    def get(self, request, keyword):
        searched_by_title = SsafyArticle.objects.filter(title__icontains=keyword)
        searched_by_content = SsafyArticle.objects.filter(content__icontains=keyword)
        searched_by_tag = SsafyArticle.objects.none()
        for tag in Tag.objects.filter(name__icontains=keyword):
            searched_by_tag = searched_by_tag.union(tag.ssafy_articles.all())

        searched_articles = searched_by_title.union(searched_by_content).union(searched_by_tag).order_by('-created_at')
        serializer = SsafyArticleListSerializer(searched_articles, many=True)
        return Response(serializer.data)

########################

### 자유게시판
class FreeArticleListView(APIView):
    # Free ArticleList
    def get(self, request):
        articles = FreeArticle.objects.order_by('-created_at')
        serializer = FreeArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    # Free ArticleCreate
    def post(self, request):
        serializer = FreeArticleDetailSerializer(data=request.data['body'])
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            article = get_object_or_404(FreeArticle, id=serializer.data['id'])
            for tag_name in request.data['tags']:
                try:
                    tag = get_object_or_404(Tag, name=tag_name)
                except:
                    tag = Tag()
                    tag.name = tag_name
                    tag.save()
                freearticletag = FreeArticleTag()
                freearticletag.article = article
                freearticletag.tag = tag
                freearticletag.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class FreeArticleDetailView(APIView):
    # Free ArticleDetail
    def get(self, request, article_id):
        article = get_article(FreeArticle, article_id)
        article.hit += 1
        article.save()
        serializer = FreeArticleDetailSerializer(article)
        return Response(serializer.data)

    # Free ArticleUpdate
    def put(self, request, article_id):
        article = get_article(FreeArticle, article_id)
        for freearticletag in FreeArticleTag.objects.filter(article=article):
            freearticletag.delete()

        serializer = FreeArticleDetailSerializer(article, data=request.data['body'])
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            for tag_name in request.data['tags']:
                try:
                    tag = get_object_or_404(Tag, name=tag_name)
                except:
                    tag = Tag()
                    tag.name = tag_name
                    tag.save()
                freearticletag = FreeArticleTag()
                freearticletag.article = article
                freearticletag.tag = tag
                freearticletag.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # Free ArticleDelete
    def delete(self, request, article_id):
        article = get_article(FreeArticle, article_id)
        article.delete()
        return Response()

class FreeArticleCommentListView(APIView):
    # Free ArticleCommentList
    def get(self, request, article_id):
        article = get_article(FreeArticle, article_id)
        serializer = FreeArticleCommentSerializer(article.comments, many=True)
        return Response(serializer.data)

    # Free ArticleCommentCreate
    def post(self, request, article_id):
        article = get_article(FreeArticle, article_id)
        serializer = FreeArticleCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, article=article)
            return Response(serializer.data)
        return Response(serializer.errors)

class FreeArticleCommentDetailView(APIView):
    # Free ArticleCommentUpdate
    def put(self, request, article_id, comment_id):
        comment = get_comment(FreeArticleComment, comment_id)
        serializer = FreeArticleCommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # Free ArticleCommentDelete
    def delete(self, request, article_id, comment_id):
        comment = get_comment(FreeArticleComment, comment_id)
        comment.delete()
        return Response()

class FreeArticleLikeView(APIView):
    # Free ArticleLike
    def post(self, request, article_id):
        article = get_article(FreeArticle, article_id)
        if article.like_users.filter(id=request.user.id).exists():
            articlelike = get_object_or_404(FreeArticleLike, user=request.user, article=article)
            articlelike.delete()
        else:
            articlelike = FreeArticleLike()
            articlelike.user = request.user
            articlelike.article = article
            articlelike.save()
        return Response()

class FreeArticleSearchView(APIView):
    def get(self, request, keyword):
        searched_by_title = FreeArticle.objects.filter(title__icontains=keyword)
        searched_by_content = FreeArticle.objects.filter(content__icontains=keyword)
        searched_by_tag = FreeArticle.objects.none()
        for tag in Tag.objects.filter(name__icontains=keyword):
            searched_by_tag = searched_by_tag.union(tag.free_articles.all())

        searched_articles = searched_by_title.union(searched_by_content).union(searched_by_tag).order_by('-created_at')
        serializer = FreeArticleListSerializer(searched_articles, many=True)
        return Response(serializer.data)

########################

class GlobalArticleSearchView(APIView):
    def get(self, request, keyword):
        ssafy_searched_by_title = SsafyArticle.objects.filter(title__icontains=keyword)
        ssafy_searched_by_content = SsafyArticle.objects.filter(content__icontains=keyword)
        ssafy_searched_articles = ssafy_searched_by_title.union(ssafy_searched_by_content)

        free_searched_by_title = FreeArticle.objects.filter(title__icontains=keyword)
        free_searched_by_content = FreeArticle.objects.filter(content__icontains=keyword)
        free_searched_articles = free_searched_by_title.union(free_searched_by_content)
        
        total_searched_articles = ssafy_searched_articles.union(free_searched_articles)

        serializer = SsafyArticleListSerializer(total_searched_articles, many=True)
        return Response(serializer.data)