# Generated by Django 4.2 on 2023-04-24 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0014_remove_subject_end_time_remove_subject_room_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='subjects',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='timetable.subject'),
        ),
    ]
