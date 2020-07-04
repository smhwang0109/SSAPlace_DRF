from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('myaccount/', views.MyAccount.as_view()),
    path('', views.UserListView.as_view()),
    path('<int:user_pk>/', views.Profile),
    path('<int:user_pk>/edit/', views.ProfileEdit.as_view()),
]