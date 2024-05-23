# Generated by Django 5.0.4 on 2024-05-22 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_remove_notification_match_alter_notification_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='status',
            field=models.CharField(choices=[('completed', 'completed'), ('in-progress', 'in-progress'), ('rejected', 'rejected')], default='in-progress', max_length=50),
        ),
    ]