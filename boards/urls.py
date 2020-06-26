from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('<int:board_id>/', views.ArticleListView.as_view()),
    path('articles/<int:article_id>/', views.ArticleDetailView.as_view()),
    path('articles/<int:article_id>/comments/', views.ArticleCommentListView.as_view()),
    path('articles/<int:article_id>/comments/<int:comment_id>/', views.ArticleCommentDetailView.as_view()),
    path('articles/<int:article_id>/like/', views.ArticleLikeView.as_view()),
    path('articles/search/<str:keyword>/', views.ArticleSearchView.as_view()),
]