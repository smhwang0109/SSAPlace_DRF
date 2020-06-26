from django.contrib import admin
from .models import Board, Article, ArticleLike, ArticleComment

admin.site.register(Board)
admin.site.register(Article)
admin.site.register(ArticleLike)
admin.site.register(ArticleComment)