from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .models import Team, CollectTeam, CollectMember
from .serializers import TeamSerializer, CollectTeamSerializer, CollectMemberSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

def get_team(team_id):
    return get_object_or_404(Team, id=team_id)

class TeamListView(APIView):
    # TeamList
    def get(self, request):
        teams = Team.objects.all()
        teams = sorted(teams, key=lambda team: team.popularity, reverse=True)
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)
    
    # TeamCreate
    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(leader=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
    
class TeamDetailView(APIView):
    # TeamDetail
    def get(self, request, team_id):
        team = get_team(team_id)
        serializer = TeamSerializer(team)
        return Response(serializer.data)
    
    # TeamUpdate
    def put(self, request, team_id):
        team = get_team(team_id)
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # TeamDelete
    def delete(self, request, team_id):
        team = self.get_team(team_id)
        team.delete()
        return Response()

        


def get_collect_team(collect_team_id):
    return get_object_or_404(CollectTeam, id=collect_team_id)

class CollectTeamListView(APIView):
    # CollectTeamList
    def get(self, request):
        collect_teams = CollectTeam.objects.all()
        collect_teams = sorted(collect_teams, key=lambda collect_team: collect_team.popularity, reverse=True)
        serializer = CollectTeamSerializer(collect_teams, many=True)
        return Response(serializer.data)
    
class CollectTeamCreateView(APIView):
    # CollectTeamCreate
    def post(self, request, team_id):
        team = get_object_or_404(Team, pk=team_id)
        serializer = CollectTeamSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(team=team)
            return Response(serializer.data)
        return Response(serializer.errors)

class CollectMemberCreateView(APIView):
    # CollectMemberCreate
    def post(self, request, team_id, collect_team_id):
        collect_team = get_object_or_404(CollectTeam, pk=collect_team_id)
        serializer = CollectMemberSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(collect_team=collect_team)
            return Response(serializer.data)
        return Response(serializer.errors)

class CollectTeamDetailView(APIView):
    # CollectTeamDetail
    def get(self, request, collect_team_id):
        collect_team = get_collect_team(collect_team_id)
        serializer = CollectTeamSerializer(collect_team)
        return Response(serializer.data)

    # CollectTeamUpdate
    def put(self, request, collect_team_id):
        collect_team = get_collect_team(collect_team_id)
        serializer = CollectTeamSerializer(collect_team, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # CollectTeamDelete
    def delete(self, request, collect_team_id):
        collect_team = self.get_collect_team(collect_team_id)
        collect_team.delete()
        return Response()