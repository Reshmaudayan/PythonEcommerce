# Generated by Django 3.2.9 on 2022-04-09 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_remove_cartitem_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
