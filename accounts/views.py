from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .models import User
from .serializers import UserSerializer, UserProfileSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

class MyAccount(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class Profile(APIView):
    def get(self, request):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

class ProfileEdit(APIView):
    def put(self, request, user_pk):
        user = request.user
        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
