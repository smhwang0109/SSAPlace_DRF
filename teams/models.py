from django.db import models
from django.conf import settings

from datetime import datetime
from pytz import utc

# 부분 모델들

class Interest(models.Model):
    interest = models.CharField(max_length=30)

class UseLanguage(models.Model):
    language = models.CharField(max_length=20)


# 본 모델들

# 팀 정보
class Team(models.Model):
    name = models.CharField(max_length=200)
    oneline_description = models.CharField(max_length=300)
    description = models.TextField()
    leader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='leading_teams')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='teams', through='TeamMember')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 관심 분야
    interests = models.ManyToManyField(Interest, related_name='teams', through='TeamInterest')
    # 현재 팀원 수
    current_members = models.IntegerField()
    # 주 모임지역
    residence = models.CharField(max_length=100)
    # 주 사용 언어/프레임워크
    front_language = models.ManyToManyField(UseLanguage, related_name='front_languages', through='FrontUse')
    back_language = models.ManyToManyField(UseLanguage, related_name='back_languages', through='BackUse')
    # 팀 관심
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_teams', through='TeamLike')
    # 팀 로고(나중에)

    # 인기도
    @property
    def popularity(self):
        now = datetime.utcnow()
        during_time = (utc.localize(now) - self.created_at).total_seconds() + 3600
        return (self.like_users.count() + 1) / during_time

# 모집 공고
class CollectTeam(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    oneline_description = models.CharField(max_length=300, default='')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 연락처
    contact = models.CharField(max_length=11)
    # 공개 설정
    open = models.BooleanField(default=True)
    # 모집 인원
    collect_count = models.IntegerField()
    # 팀 모집 관심
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_collect_teams', through='CollectTeamLike')

    # 인기도
    @property
    def popularity(self):
        now = datetime.utcnow()
        during_time = (utc.localize(now) - self.created_at).total_seconds() + 3600
        return (self.like_users.count() + 1) / during_time
        
# 희망 팀원 상세
class CollectMember(models.Model):
    collect_team = models.ForeignKey(CollectTeam, on_delete=models.CASCADE, related_name='collect_members')
    ## 희망 팀원 역할(백, 프론트)
    role = models.CharField(max_length=30, default='무관')
    ## 사용 언어
    use_language = models.ManyToManyField(UseLanguage, related_name='collect_members', through='CollectMemberLanguage')
    ## 전공/비전공
    major = models.CharField(max_length=10, default='무관')
    # 우대 조건
    preferential = models.TextField(null=True)





# 중간 모델들

class TeamInterest(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)

class FrontUse(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    front_language = models.ForeignKey(UseLanguage, on_delete=models.CASCADE)

class BackUse(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    back_language = models.ForeignKey(UseLanguage, on_delete=models.CASCADE)

class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class TeamLike(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    like_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class CollectTeamLike(models.Model):
    collect_team = models.ForeignKey(CollectTeam, on_delete=models.CASCADE)
    like_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class CollectMemberLanguage(models.Model):
    collect_member = models.ForeignKey(CollectMember, on_delete=models.CASCADE)
    use_language = models.ForeignKey(UseLanguage, on_delete=models.CASCADE)