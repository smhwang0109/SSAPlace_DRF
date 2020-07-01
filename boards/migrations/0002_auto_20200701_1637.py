# Generated by Django 2.1.15 on 2020-07-01 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hit', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='free_articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FreeArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='free_comments', to='boards.FreeArticle')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='free_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FreeArticleLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.FreeArticle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SsafyArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hit', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ssafy_articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SsafyArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ssafy_comments', to='boards.SsafyArticle')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ssafy_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SsafyArticleLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.SsafyArticle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='board',
        ),
        migrations.RemoveField(
            model_name='article',
            name='like_users',
        ),
        migrations.RemoveField(
            model_name='articlecomment',
            name='article',
        ),
        migrations.RemoveField(
            model_name='articlecomment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='articlelike',
            name='article',
        ),
        migrations.RemoveField(
            model_name='articlelike',
            name='user',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='ArticleComment',
        ),
        migrations.DeleteModel(
            name='ArticleLike',
        ),
        migrations.DeleteModel(
            name='Board',
        ),
        migrations.AddField(
            model_name='ssafyarticle',
            name='like_users',
            field=models.ManyToManyField(related_name='ssafy_like_articles', through='boards.SsafyArticleLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='freearticle',
            name='like_users',
            field=models.ManyToManyField(related_name='free_like_articles', through='boards.FreeArticleLike', to=settings.AUTH_USER_MODEL),
        ),
    ]
