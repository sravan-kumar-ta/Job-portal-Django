# Generated by Django 5.0.7 on 2024-08-24 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_job_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
