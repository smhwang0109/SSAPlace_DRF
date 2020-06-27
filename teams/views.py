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
    
    # def post(self, request, team_id):
    #     team = get_team(team_id)

        


def get_collect_team(collect_team_id):
    return get_object_or_404(CollectTeam, id=collect_team_id)

class CollectTeamListView(APIView):
    # CollectTeamList
    def get(self, request):
        collectTeams = CollectTeam.objects.all()
        collectTeams = sorted(collectTeams, key=lambda collectTeam: collectTeam.popularity, reverse=True)

        serializer = CollectTeamSerializer(collectTeams, many=True)
        return Response(serializer.data)
    
    # CollectTeamCreate
    def post(self, request, team_id):
        team = get_object_or_404(Team, pk=team_id)
        serializer = CollectTeamSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(team=team)
            return Response(serializer.data)
        return Response(serializer.errors)

# class ArticleDetailView(APIView):
#     # ArticleDetail
#     def get(self, request, article_id):
#         article = get_article(article_id)
#         article.hit += 1
#         article.save()
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     # ArticleUpdate
#     def put(self, request, article_id):
#         article = get_article(article_id)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     # ArticleDelete
#     def delete(self, request, article_id):
#         article = self.get_article(article_id)
#         article.delete()
#         return Response()