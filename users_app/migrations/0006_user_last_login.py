# Generated by Django 4.2.4 on 2023-08-26 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0005_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
