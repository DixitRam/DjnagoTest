# Generated by Django 5.0.2 on 2024-02-25 15:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('wind_speed', models.FloatField()),
                ('wind_direction', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FarmDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('piece', models.IntegerField()),
                ('abw', models.FloatField()),
                ('gain', models.FloatField()),
                ('adg', models.FloatField()),
                ('date', models.DateField()),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShrimpEasy.farm')),
            ],
        ),
        migrations.AddField(
            model_name='farm',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShrimpEasy.user'),
        ),
    ]