from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    ### Tags
    path('tags/', views.TagListView.as_view()),

    ### Boards
    path('<str:board_name>/', views.ArticleListView.as_view()),
    path('<str:board_name>/<int:article_id>/', views.ArticleDetailView.as_view()),
    path('<str:board_name>/<int:article_id>/comments/', views.ArticleCommentListView.as_view()),
    path('<str:board_name>/<int:article_id>/comments/<int:comment_id>/', views.ArticleCommentDetailView.as_view()),
    path('<str:board_name>/<int:article_id>/like/', views.ArticleLikeView.as_view()),
    path('<str:board_name>/search/<str:filter_name>/<str:keyword>/', views.ArticleSearchView.as_view()),
]
