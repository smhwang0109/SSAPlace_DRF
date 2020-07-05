# Generated by Django 2.1.15 on 2020-07-05 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20200701_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.FreeArticle')),
            ],
        ),
        migrations.CreateModel(
            name='SsafyArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.SsafyArticle')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='freearticlecomment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='boards.FreeArticle'),
        ),
        migrations.AlterField(
            model_name='ssafyarticlecomment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='boards.SsafyArticle'),
        ),
        migrations.AddField(
            model_name='ssafyarticletag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Tag'),
        ),
        migrations.AddField(
            model_name='freearticletag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Tag'),
        ),
        migrations.AddField(
            model_name='freearticle',
            name='tags',
            field=models.ManyToManyField(related_name='free_articles', through='boards.FreeArticleTag', to='boards.Tag'),
        ),
        migrations.AddField(
            model_name='ssafyarticle',
            name='tags',
            field=models.ManyToManyField(related_name='ssafy_articles', through='boards.SsafyArticleTag', to='boards.Tag'),
        ),
    ]
