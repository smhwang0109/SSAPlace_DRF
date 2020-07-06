from django.contrib import admin
from .models import Tag, SsafyArticle, SsafyArticleComment, SsafyArticleLike, SsafyArticleTag, FreeArticle, FreeArticleComment, FreeArticleLike, FreeArticleTag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

### 싸피 게시판
class SsafyArticleCommentInline(admin.StackedInline):
    model = SsafyArticleComment

class SsafyArticleLikeInline(admin.StackedInline):
    model = SsafyArticleLike

class SsafyArticleTagInline(admin.StackedInline):
    model = SsafyArticleTag

@admin.register(SsafyArticle)
class SsafyArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at', 'updated_at', 'hit', 'author']
    list_display_links = ['id', 'title', 'content', 'created_at', 'updated_at', 'hit', 'author']
    inlines = [SsafyArticleCommentInline, SsafyArticleLikeInline, SsafyArticleTagInline]


### 자유 게시판
class FreeArticleCommentInline(admin.StackedInline):
    model = FreeArticleComment

class FreeArticleLikeInline(admin.StackedInline):
    model = FreeArticleLike

class FreeArticleTagInline(admin.StackedInline):
    model = FreeArticleTag

@admin.register(FreeArticle)
class FreeArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at', 'updated_at', 'hit', 'author']
    list_display_links = ['id', 'title', 'content', 'created_at', 'updated_at', 'hit', 'author']
    inlines = [FreeArticleCommentInline, FreeArticleLikeInline, FreeArticleTagInline]