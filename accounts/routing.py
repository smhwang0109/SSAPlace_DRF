from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('chat/<str:message>/', consumers.ChatConsumer),
]