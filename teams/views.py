from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .models import Team, CollectTeam, CollectMember, Interest, UseLanguage, TeamMember, TeamInterest, FrontUse, BackUse, CollectMemberLanguage
from .serializers import TeamSerializer, CollectTeamSerializer, CollectMemberSerializer, InterestSerializer, UseLanguageSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

def get_team(team_id):
    return get_object_or_404(Team, id=team_id)

def get_collect_team(team):
    return get_object_or_404(CollectTeam, team=team)

def get_user(user_id):
    User = get_user_model()
    return get_object_or_404(User, id=user_id)

class TeamProfileListView(APIView):
    # TeamList
    def get(self, request, user_id):
        user = get_user(user_id)
        teams = Team.objects.filter(members=user).distinct()
        teams = sorted(teams, key=lambda team: team.updated_at, reverse=True)
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)
    
class TeamListView(APIView):
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
            team.members.clear()
            team.interests.clear()
            team.front_language.clear()
            team.back_language.clear()
            User = get_user_model()
            for member_id in request.data['members']:
                member = get_object_or_404(User, id=member_id)
                if not TeamMember.objects.filter(team=team, member=member).exists():
                    team_interest = TeamMember()
                    team_interest.team = team
                    team_interest.member = member
                    team_interest.save()
            for interest_id in request.data['interests']:
                interest = get_object_or_404(Interest, id=interest_id)
                if not TeamInterest.objects.filter(team=team, interest=interest).exists():
                    team_interest = TeamInterest()
                    team_interest.team = team
                    team_interest.interest = interest
                    team_interest.save()
            for front_id in request.data['front_language']:
                front = get_object_or_404(UseLanguage, id=front_id)
                if not FrontUse.objects.filter(team=team, front_language=front).exists():
                    team_front = FrontUse()
                    team_front.team = team
                    team_front.front_language = front
                    team_front.save()
            for back_id in request.data['back_language']:
                back = get_object_or_404(UseLanguage, id=back_id)
                if not BackUse.objects.filter(team=team, back_language=back).exists():
                    team_back = BackUse()
                    team_back.team = team
                    team_back.back_language = back
                    team_back.save()

            return Response(serializer.data)
        return Response(serializer.errors)
    
    # TeamDelete
    def delete(self, request, team_id):
        team = self.get_team(team_id)
        team.delete()
        return Response()

        


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
        serializer = CollectTeamSerializer(data=request.data[0])
        if serializer.is_valid(raise_exception=True):
            serializer.save(team=team)
            # CollectMemberCreate
            collect_team = get_object_or_404(CollectTeam, id=serializer.data['id'])
            for i in range(1, len(request.data)):
                serializer = CollectMemberSerializer(data=request.data[i])
                if serializer.is_valid(raise_exception=True):
                    serializer.save(collect_team=collect_team)
                    collect_member = get_object_or_404(CollectMember, id=serializer.data['id'])
                    for language_id in request.data[i]['use_language']:
                        language = get_object_or_404(UseLanguage, id=language_id)
                        language_use = CollectMemberLanguage()
                        language_use.collect_member = collect_member
                        language_use.use_language = language
                        language_use.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CollectTeamDetailView(APIView):
    # CollectTeamDetail
    def get(self, request, team_id):
        team = get_team(team_id)
        collect_team = get_collect_team(team)
        serializer = CollectTeamSerializer(collect_team)
        return Response(serializer.data)

    # CollectTeamUpdate
    def put(self, request, team_id):
        team = get_team(team_id)
        collect_team = get_collect_team(team)
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

class UseLanguageListView(APIView):
    def get(self, request):
        use_languages = UseLanguage.objects.all()
        serializer = UseLanguageSerializer(use_languages, many=True)
        return Response(serializer.data)
        