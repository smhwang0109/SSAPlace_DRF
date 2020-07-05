from django.contrib import admin
from .models import SsafyArticle, SsafyArticleComment, SsafyArticleLike, FreeArticle, FreeArticleComment, FreeArticleLike, Tag

admin.site.register(SsafyArticle)
admin.site.register(SsafyArticleComment)
admin.site.register(SsafyArticleLike)
admin.site.register(FreeArticle)
admin.site.register(FreeArticleComment)
admin.site.register(FreeArticleLike)
admin.site.register(Tag)