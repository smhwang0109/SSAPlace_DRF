from django.core import serializers as django_serializers

from django.contrib.auth import get_user_model
from rest_framework import serializers

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
    
    
class UserProfileSerializer(serializers.ModelSerializer):
    # 자기소개, 위치, 웹사이트 주소 (페이스북, 인스타그램, github, 개인홈페이지, linkedin), email, languages, skills, team
    # self_introduction = serializers.CharField()
    # location = serializers.CharField()
    # email = serializers.EmailField()
    # instagram = serializers.URLField()
    # github = serializers.URLField() 
    # facebook = serializers.URLField()
    # homepage = serializers.URLField()
    # linkedin = serializers.URLField() 
    # teams = serializers.SerializerMethodField()
    # languages = serializers.SerializerMethodField()
    # skills = serializers.SerializerMethodField()
    class Meta:
        model = User
        exclude = ['password',]
    
    def get_teams(self, obj):
        team = obj.teams.all() 
        return django_serializers.serializer('json', team)
    
    # def get_skills(self, obj):
    #     skill = obj.
    # articles = serializers.SerializerMethodField()
    # like_articles = serializers.SerializerMethodField()

    # def get_articles(self, obj):
    #     return django_serializers.serialize('json', obj.articles.order_by('-created_at'), ensure_ascii=False)

    # def get_like_articles(self, obj):
    #     return django_serializers.serialize('json', obj.like_articles.order_by('-created_at'), ensure_ascii=False)
    
    