from django.core import serializers as django_serializers

from rest_framework import serializers
from .models import Team, CollectTeam, CollectMember, Interest, UseLanguage
from accounts.serializers import UserSerializer

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'

class UseLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseLanguage
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    leader = UserSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)

    class Meta:
        model = Team
        fields = '__all__'

class CollectTeamSerializer(serializers.ModelSerializer):
    team = TeamSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)

    collect_members = serializers.SerializerMethodField()
    
    class Meta:
        model = CollectTeam
        fields = '__all__'

    def get_collect_members(self, obj):
        return django_serializers.serialize('json', obj.collect_members.all(), ensure_ascii=False)

class CollectMemberSerializer(serializers.ModelSerializer):
    collect_team = CollectTeamSerializer(required=False)

    class Meta:
        model = CollectMember
        fields = '__all__'
