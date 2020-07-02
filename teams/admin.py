from django.contrib import admin
from .models import Team, CollectTeam, CollectMember, Interest, CollectMemberMajor, CollectMemberRole, UseLanguage, TeamInterest, TeamMember


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'interest')
    list_display_links = ('id', 'interest')

@admin.register(TeamInterest)
class TeamInterestAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

@admin.register(UseLanguage)
class UseLanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'language')
    list_display_links = ('id', 'language')

class CollectMemberInline(admin.StackedInline):
    model = CollectMember

class CollectTeamInline(admin.StackedInline):
    model = CollectTeam

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'oneline_description', 'leader')
    list_display_links = ('id', 'name', 'oneline_description', 'leader')
    inlines = [CollectTeamInline]

@admin.register(CollectTeam)
class CollectTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title', 'description')
    inlines = [CollectMemberInline]