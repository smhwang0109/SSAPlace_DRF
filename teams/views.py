from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .models import Team, CollectTeam, CollectMember, Interest, Role, Major, UseLanguage, TeamMember, TeamInterest, FrontUse, BackUse
from .serializers import TeamSerializer, CollectTeamSerializer, CollectMemberSerializer, InterestSerializer, RoleSerializer, MajorSerializer, UseLanguageSerializer

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
            User = get_user_model()
            team = get_object_or_404(Team, id=serializer.data['id'])
            for member_id in request.data['members']:
                member = get_object_or_404(User, id=member_id)
                team_member = TeamMember()
                team_member.team = team
                team_member.member = member
                team_member.save()
            for interest_id in request.data['interests']:
                interest = get_object_or_404(Interest, id=interest_id)
                print(interest_id, interest)
                team_interest = TeamInterest()
                team_interest.team = team
                team_interest.interest = interest
                team_interest.save()
            for front_id in request.data['front_language']:
                front = get_object_or_404(UseLanguage, id=front_id)
                front_use = FrontUse()
                front_use.team = team
                front_use.front_language = front
                front_use.save()
            for back_id in request.data['back_language']:
                back = get_object_or_404(UseLanguage, id=back_id)
                back_use = BackUse()
                back_use.team = team
                back_use.back_language = back
                back_use.save()
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




# 부분 모델 가져오기

class InterestListView(APIView):
    def get(self, request):
        interests = Interest.objects.all()
        serializer = InterestSerializer(interests, many=True)
        return Response(serializer.data)

class RoleListView(APIView):
    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

class MajorListView(APIView):
    def get(self, request):
        majors = Major.objects.all()
        serializer = MajorSerializer(majors, many=True)
        return Response(serializer.data)

class UseLanguageListView(APIView):
    def get(self, request):
        use_languages = UseLanguage.objects.all()
        serializer = UseLanguageSerializer(use_languages, many=True)
        return Response(serializer.data)
        