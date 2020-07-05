from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

def get_profile(user_pk):
    return get_object_or_404(Profile, user=user_pk)

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

class ProfileList(APIView):
    def post(self, request):
        serializer = ProfileSerializer()
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

class ProfileDetail(APIView):
    def get(self, request, user_pk):
        profile = get_profile(user_pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, user_pk):
        profile = get_profile(user_pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
