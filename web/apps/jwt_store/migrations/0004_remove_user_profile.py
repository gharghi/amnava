# Generated by Django 3.0.dev20190224003410 on 2019-04-13 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_store', '0003_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile',
        ),
    ]
