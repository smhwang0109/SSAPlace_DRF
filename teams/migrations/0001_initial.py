# Generated by Django 3.0.7 on 2020-06-28 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BackUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CollectMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferential', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CollectTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact', models.CharField(max_length=11)),
                ('open', models.BooleanField()),
                ('collectCount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FrontUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Major', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('무관', '무관'), ('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Fullstack', 'Fullstack')], default='무관', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('oneline_description', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('currentMembers', models.IntegerField()),
                ('finalMembers', models.IntegerField()),
                ('residence', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UseLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team')),
            ],
        ),
        migrations.CreateModel(
            name='TeamLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team')),
            ],
        ),
        migrations.CreateModel(
            name='TeamInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Interest')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='back_language',
            field=models.ManyToManyField(related_name='back_languages', through='teams.BackUse', to='teams.UseLanguage'),
        ),
        migrations.AddField(
            model_name='team',
            name='front_language',
            field=models.ManyToManyField(related_name='front_languages', through='teams.FrontUse', to='teams.UseLanguage'),
        ),
        migrations.AddField(
            model_name='team',
            name='interests',
            field=models.ManyToManyField(related_name='teams', through='teams.TeamInterest', to='teams.Interest'),
        ),
        migrations.AddField(
            model_name='team',
            name='leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leading_teams', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='team',
            name='like_users',
            field=models.ManyToManyField(related_name='like_teams', through='teams.TeamLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(related_name='teams', through='teams.TeamMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='frontuse',
            name='front_language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.UseLanguage'),
        ),
        migrations.AddField(
            model_name='frontuse',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team'),
        ),
        migrations.CreateModel(
            name='CollectTeamLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collect_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.CollectTeam')),
                ('like_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='collectteam',
            name='like_users',
            field=models.ManyToManyField(related_name='like_collect_teams', through='teams.CollectTeamLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='collectteam',
            name='team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teams.Team'),
        ),
        migrations.CreateModel(
            name='CollectMemberRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collect_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.CollectMember')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Role')),
            ],
        ),
        migrations.CreateModel(
            name='CollectMemberMajor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collect_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.CollectMember')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Major')),
            ],
        ),
        migrations.CreateModel(
            name='CollectMemberLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collect_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.CollectMember')),
                ('use_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.UseLanguage')),
            ],
        ),
        migrations.AddField(
            model_name='collectmember',
            name='collect_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collect_members', to='teams.CollectTeam'),
        ),
        migrations.AddField(
            model_name='collectmember',
            name='major',
            field=models.ManyToManyField(related_name='collect_members', through='teams.CollectMemberMajor', to='teams.Major'),
        ),
        migrations.AddField(
            model_name='collectmember',
            name='role',
            field=models.ManyToManyField(related_name='collect_members', through='teams.CollectMemberRole', to='teams.Role'),
        ),
        migrations.AddField(
            model_name='collectmember',
            name='use_language',
            field=models.ManyToManyField(related_name='collect_members', through='teams.CollectMemberLanguage', to='teams.UseLanguage'),
        ),
        migrations.AddField(
            model_name='backuse',
            name='back_language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.UseLanguage'),
        ),
        migrations.AddField(
            model_name='backuse',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team'),
        ),
    ]
