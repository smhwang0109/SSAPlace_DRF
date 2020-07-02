from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('myaccount/', views.MyAccount.as_view()),
    path('', views.UserListView.as_view()),
]