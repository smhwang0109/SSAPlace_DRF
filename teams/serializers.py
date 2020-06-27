from django.core import serializers as django_serializers

from rest_framework import serializers
from .models import Team, CollectTeam, CollectMember
from accounts.serializers import UserSerializer

class TeamSerializer(serializers.ModelSerializer):
    leader = UserSerializer(required=False)

    class Meta:
        model = Team
        fields = '__all__'

class CollectTeamSerializer(serializers.ModelSerializer):
    team = TeamSerializer(required=False)

    class Meta:
        model = CollectTeam
        fields = '__all__'

class CollectMemberSerializer(serializers.ModelSerializer):
    collectTeam = CollectTeamSerializer(required=False)

    class Meta:
        model = CollectMember
        fields = '__all__'
