# Generated by Django 5.0.4 on 2024-06-15 10:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_alter_notification_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
