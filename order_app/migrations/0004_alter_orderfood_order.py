# Generated by Django 4.2.4 on 2023-08-23 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0003_order_telegram_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderfood',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Order_orderfood', to='order_app.order'),
        ),
    ]