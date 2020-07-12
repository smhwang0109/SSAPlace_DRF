# Generated by Django 2.1.15 on 2020-07-07 14:26

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
            name='CodeArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hit', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='code_articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CodeArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='boards.CodeArticle')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='code_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CodeArticleLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.CodeArticle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CodeArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.CodeArticle')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Tag')),
            ],
        ),
        migrations.AlterField(
            model_name='ssafyarticle',
            name='like_users',
            field=models.ManyToManyField(related_name='ssafy_like_articles', through='boards.SSAFYArticleLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ssafyarticle',
            name='tags',
            field=models.ManyToManyField(related_name='ssafy_articles', through='boards.SSAFYArticleTag', to='boards.Tag'),
        ),
        migrations.AlterField(
            model_name='ssafyarticlecomment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='boards.SSAFYArticle'),
        ),
        migrations.AlterField(
            model_name='ssafyarticlelike',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.SSAFYArticle'),
        ),
        migrations.AlterField(
            model_name='ssafyarticletag',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.SSAFYArticle'),
        ),
        migrations.AddField(
            model_name='codearticle',
            name='like_users',
            field=models.ManyToManyField(related_name='code_like_articles', through='boards.CodeArticleLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='codearticle',
            name='tags',
            field=models.ManyToManyField(related_name='code_articles', through='boards.CodeArticleTag', to='boards.Tag'),
        ),
    ]