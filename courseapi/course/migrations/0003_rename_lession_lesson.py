# Generated by Django 5.1.6 on 2025-02-28 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_lession'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lession',
            new_name='Lesson',
        ),
    ]
