# Generated by Django 3.2.13 on 2022-07-14 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
    ]
