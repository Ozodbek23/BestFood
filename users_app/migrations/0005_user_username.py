# Generated by Django 4.2.4 on 2023-08-25 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0004_user_email_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]