# Generated by Django 4.2.3 on 2023-08-22 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='food',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]