# Generated by Django 5.0.7 on 2024-09-11 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0003_alter_resume_resume_alter_seekerprofile_bio_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='user',
            new_name='seeker',
        ),
    ]
