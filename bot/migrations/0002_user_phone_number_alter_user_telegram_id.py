# Generated by Django 5.1 on 2024-08-16 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='telegram_id',
            field=models.IntegerField(unique=True),
        ),
    ]
