from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    path('', views.TeamListView.as_view()),
    path('<int:team_id>/', views.TeamDetailView.as_view()),
    path('collect/', views.CollectTeamListView.as_view())
]