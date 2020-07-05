from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    ### SSAFY
    path('ssafy/', views.SsafyArticleListView.as_view()),
    path('ssafy/<int:article_id>/', views.SsafyArticleDetailView.as_view()),
    path('ssafy/<int:article_id>/comments/', views.SsafyArticleCommentListView.as_view()),
    path('ssafy/<int:article_id>/comments/<int:comment_id>/', views.SsafyArticleCommentDetailView.as_view()),
    path('ssafy/<int:article_id>/like/', views.SsafyArticleLikeView.as_view()),
    path('ssafy/search/<str:keyword>/', views.SsafyArticleSearchView.as_view()),

    ### Free
    path('free/', views.FreeArticleListView.as_view()),
    path('free/<int:article_id>/', views.FreeArticleDetailView.as_view()),
    path('free/<int:article_id>/comments/', views.FreeArticleCommentListView.as_view()),
    path('free/<int:article_id>/comments/<int:comment_id>/', views.FreeArticleCommentDetailView.as_view()),
    path('free/<int:article_id>/like/', views.FreeArticleLikeView.as_view()),
    path('free/search/<str:keyword>/', views.FreeArticleSearchView.as_view()),

    ### Global Article Search
    path('search/<str:keyword>/', views.GlobalArticleSearchView.as_view()),

    ### Tags
    path('tags/', views.TagListView.as_view()),
]