# Generated by Django 3.0.dev20190224003410 on 2019-04-13 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]