# Generated by Django 3.0.7 on 2020-07-14 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectmember',
            name='preferential',
            field=models.TextField(blank=True, null=True),
        ),
    ]