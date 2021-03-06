from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Q

from .models import User, Profile, ProfileInterest, ProfileLanguage, MessageGroup, Message
from teams.models import Interest, UseLanguage
from .serializers import UserSerializer, ProfileSerializer, MessageGroupSerializer, MessageSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

def get_user(user_pk):
    User = get_user_model()
    return get_object_or_404(User, pk=user_pk)

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
        
        message_groups = sorted(message_groups, key=lambda message_group: message_group.message_updated_at, reverse=True)
        user_list = []
        group_dict = {}
        cnt = 1
        for message_group in message_groups:
            if message_group.to_user != request.user and message_group.to_user.id not in user_list:
                user_list.append(message_group.to_user.id)
                group_dict[cnt] = {'id': message_group.to_user.id, 'username': message_group.to_user.username}
                cnt += 1
            elif message_group.from_user != request.user and message_group.from_user.id not in user_list:
                user_list.append(message_group.from_user.id)
                group_dict[cnt] = {'id': message_group.from_user.id, 'username': message_group.from_user.username}
                cnt += 1
        serializer = group_dict
        return Response(serializer)
    
    def post(self, request):
        user = get_user(request.data['to_user'])
        message_group = MessageGroup()
        message_group.from_user = request.user
        message_group.to_user = user
        message_group.save()
        return Response()

class MessageDetailView(APIView):
    def get(self, request, to_user_id):
        to_user = get_user(to_user_id)
        message_groups = MessageGroup.objects.filter(Q(to_user=request.user, from_user=to_user)|Q(from_user=request.user, to_user=to_user))
        messages = Message.objects.none()
        for message_group in message_groups:
            messages = messages.union(message_group.messages.all()).order_by('-created_at')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    
    # def post(self, request, to_user_id):
    #     user = get_user(request.data['to_user'])
    #     message_group = MessageGroup()
    #     message_group.from_user = request.user
    #     message_group.to_user = user
    #     message_group.save()
    #     return Response()


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
                    profile_interest = ProfileInterest()
                    profile_interest.profile = profile
                    profile_interest.interest = interest
                    profile_interest.save()
            for language_id in request.data['languages']:
                language = get_object_or_404(UseLanguage, id=language_id)
                if not ProfileLanguage.objects.filter(profile=profile, language=language).exists():
                    profile_language = ProfileLanguage()
                    profile_language.profile = profile
                    profile_language.language = language
                    profile_language.save()
            return Response(serializer.data)
        return Response(serializer.errors)
