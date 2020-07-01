from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    path('', views.TeamListView.as_view()),
    path('<int:team_id>/', views.TeamDetailView.as_view()),
    path('<int:team_id>/collect/', views.CollectTeamCreateView.as_view()),
    path('<int:team_id>/collect/<int:collect_team_id>/', views.CollectMemberCreateView.as_view()),
    path('collect/', views.CollectTeamListView.as_view()),
    path('collect/<int:collect_team_id>/', views.CollectTeamDetailView.as_view()),

    # 부분 모델 가져오기
    # Interest, Role, Major, UseLanguage
    path('interest/', views.InterestListView.as_view()),
    path('role/', views.RoleListView.as_view()),
    path('major/', views.MajorListView.as_view()),
    path('uselanguage/', views.UseLanguageListView.as_view()),
]