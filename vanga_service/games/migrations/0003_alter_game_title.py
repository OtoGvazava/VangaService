# Generated by Django 4.0.3 on 2022-04-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_rename_games_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
