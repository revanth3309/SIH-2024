# Generated by Django 3.2.25 on 2024-06-08 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create_team_member',
            name='created_by',
        ),
    ]
