# Generated by Django 5.0.4 on 2024-06-18 03:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clan_pages', '0005_alter_clan_image_url'),
        ('notifications', '0005_notification_create_at_notification_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='clan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clan_pages.clan', verbose_name='Clan'),
        ),
    ]
