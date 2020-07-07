from django.core import serializers as django_serializers
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Profile, MessageGroup, Message

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password',]
    
    # articles = serializers.SerializerMethodField()
    # like_articles = serializers.SerializerMethodField()

    # def get_articles(self, obj):
    #     return django_serializers.serialize('json', obj.articles.order_by('-created_at'), ensure_ascii=False)

    # def get_like_articles(self, obj):
    #     return django_serializers.serialize('json', obj.like_articles.order_by('-created_at'), ensure_ascii=False)
    
class MessageGroupSerializer(serializers.ModelSerializer):
    from_user = UserSerializer(required=False)
    to_user = UserSerializer(required=False)

    class Meta:
        model = MessageGroup
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    message_group = MessageGroupSerializer(required=False)
    
    class Meta:
        model = Message
        fields = '__all__'
        

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Profile
        fields = '__all__'
    
    