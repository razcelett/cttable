# Generated by Django 4.2 on 2023-04-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0018_remove_room_inside_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]