# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 17:41
from __future__ import unicode_literals

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
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('is_public', models.BooleanField(default=True)),
                ('max_teams_per_league', models.PositiveIntegerField()),
                ('max_players_per_team', models.PositiveIntegerField()),
                ('max_injured_players_per_team', models.PositiveIntegerField()),
                ('points_per_match_win', models.PositiveIntegerField()),
                ('tournament_win_bonus', models.PositiveIntegerField()),
                ('grand_slam_point_multiplier', models.PositiveIntegerField()),
                ('administrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament_round', models.CharField(choices=[('128', 'Round of 128'), ('64', 'Round of 64'), ('32', 'Round of 32'), ('16', 'Round of 16'), ('8', 'Quarter-Finals'), ('4', 'Semi-Finals'), ('2', 'Finals')], max_length=10)),
                ('score', models.CharField(max_length=100)),
                ('date_played', models.DateField()),
                ('number_sets', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, unique=True)),
                ('last_name', models.CharField(max_length=30, unique=True)),
                ('date_of_birth', models.DateField()),
                ('is_injured', models.BooleanField(default=False)),
                ('world_ranking', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tennis.League')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('surface', models.CharField(choices=[('HARD', 'Hard'), ('GRASS', 'Grass'), ('CLAY', 'Clay'), ('OTHER', 'Other')], max_length=20)),
                ('tournament_level', models.CharField(choices=[('GRAND_SLAM', 'Grand Slam'), ('ATP_WORLD_TOUR_FINALS', 'ATP World Tour Finals'), ('ATP_WORLD_TOUR_MASTERS_1000', 'ATP World Tour Masters 1000'), ('ATP_WORLD_TOUR_MASTERS_500', 'ATP World Tour 500 Series'), ('ATP_WORLD_TOUR_MASTERS_250', 'ATP World Tour 250 Series'), ('ATP_CHALLENGER_TOUR', 'ATP Challenger Tour')], max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tennis.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='player1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='tennis.Player'),
        ),
        migrations.AddField(
            model_name='match',
            name='player2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='tennis.Player'),
        ),
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tennis.Tournament'),
        ),
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='tennis.Player'),
        ),
        migrations.AlterUniqueTogether(
            name='match',
            unique_together=set([('player1', 'player2', 'tournament')]),
        ),
    ]
