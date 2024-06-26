# Generated by Django 5.0.4 on 2024-06-02 07:46

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clan_pages', '0004_alter_clan_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clan',
            name='image_url',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, null=True, verbose_name='Image URL'),
        ),
    ]
