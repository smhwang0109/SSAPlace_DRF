from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

class MyAccount(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)