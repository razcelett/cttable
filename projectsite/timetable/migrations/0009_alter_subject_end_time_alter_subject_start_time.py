# Generated by Django 4.2 on 2023-04-21 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0008_remove_schedule_time_remove_subject_faculty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='end_time',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='start_time',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
