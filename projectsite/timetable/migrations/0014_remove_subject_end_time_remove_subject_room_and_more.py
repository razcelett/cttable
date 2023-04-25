# Generated by Django 4.2 on 2023-04-24 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0013_schedule_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='room',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='start_time',
        ),
        migrations.AddField(
            model_name='schedule',
            name='room',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Room', to='timetable.room'),
        ),
    ]
