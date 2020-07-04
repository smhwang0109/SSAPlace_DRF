# Generated by Django 2.1.15 on 2020-07-04 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20200701_1637'),
    ]

    operations = [
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
    ]