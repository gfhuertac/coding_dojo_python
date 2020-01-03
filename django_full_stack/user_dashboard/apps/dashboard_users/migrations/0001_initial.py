# Generated by Django 2.2 on 2020-01-03 03:30

import apps.dashboard_users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('user_level', models.IntegerField(choices=[(apps.dashboard_users.models.UserLevel(9), 9), (apps.dashboard_users.models.UserLevel(1), 1)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
