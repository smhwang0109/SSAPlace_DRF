from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Q

from .models import User, Profile, ProfileInterest, ProfileLanguage, MessageGroup
from teams.models import Interest, UseLanguage
from .serializers import UserSerializer, ProfileSerializer, MessageGroupSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

def get_profile(user_pk):
    return get_object_or_404(Profile, user=user_pk)

class MyAccount(APIView):
    def post(self, request):
        user = request.user
        serializer = UserSerializer(user)
        if not Profile.objects.filter(user=request.user.id).exists():
            profile = Profile()
            profile.user = user
            profile.save()
        return Response(serializer.data)


class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class MessageGroupListView(APIView):
    def get(self, request):
        message_groups = MessageGroup.objects.filter(Q(to_user=request.user)|Q(from_user=request.user))
        serializer = MessageGroupSerializer(message_groups, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        message_group = MessageGroup()
        message_group.from_user = request.user
        message_group.to_user = request.data['to_user']
        message_group.save()
        return Response()

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
            profile.interests.clear()
            profile.languages.clear()
            for interest_id in request.data['interests']:
                interest = get_object_or_404(Interest, id=interest_id)
                if not ProfileInterest.objects.filter(profile=profile, interest=interest).exists():
                    profile.interests.add(interest)
            for language_id in request.data['languages']:
                language = get_object_or_404(UseLanguage, id=language_id)
                if not ProfileLanguage.objects.filter(profile=profile, language=language).exists():
                    profile.languages.add(language)
            return Response(serializer.data)
        return Response(serializer.errors)
