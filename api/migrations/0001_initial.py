# Generated by Django 3.1.7 on 2021-03-24 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('jersey_no', models.IntegerField(blank=True)),
                ('current_club', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('apps', models.IntegerField(blank=True)),
                ('goals', models.IntegerField(blank=True)),
                ('wins', models.IntegerField(blank=True)),
                ('losses', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerSeasonWiseStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=50)),
                ('club', models.CharField(max_length=50)),
                ('apps', models.CharField(max_length=50)),
                ('goals', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.playerinfo')),
            ],
        ),
    ]