# Generated by Django 5.0.4 on 2024-06-13 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='memorable_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
