from django.contrib import admin
from .models import Tag, SSAFYArticle, SSAFYArticleComment, SSAFYArticleLike, SSAFYArticleTag, FreeArticle, FreeArticleComment, FreeArticleLike, FreeArticleTag, CodeArticle, CodeArticleComment, CodeArticleLike, CodeArticleTag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

### 싸피 게시판
class SSAFYArticleCommentInline(admin.StackedInline):
    model = SSAFYArticleComment

class SSAFYArticleLikeInline(admin.StackedInline):
    model = SSAFYArticleLike

class SSAFYArticleTagInline(admin.StackedInline):
    model = SSAFYArticleTag

@admin.register(SSAFYArticle)
class SSAFYArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at', 'updated_at', 'hit', 'author']
    list_display_links = ['id', 'title', 'content', 'created_at', 'updated_at', 'hit', 'author']
    inlines = [SSAFYArticleCommentInline, SSAFYArticleLikeInline, SSAFYArticleTagInline]


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


### 코드 게시판
class CodeArticleCommentInline(admin.StackedInline):
    model = CodeArticleComment

class CodeArticleLikeInline(admin.StackedInline):
    model = CodeArticleLike

class CodeArticleTagInline(admin.StackedInline):
    model = CodeArticleTag

@admin.register(CodeArticle)
class CodeArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at', 'updated_at', 'hit', 'author']
    list_display_links = ['id', 'title', 'content', 'created_at', 'updated_at', 'hit', 'author']
    inlines = [CodeArticleCommentInline, CodeArticleLikeInline, CodeArticleTagInline]