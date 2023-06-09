# Generated by Django 4.2 on 2023-04-25 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0016_alter_schedule_block_section_alter_schedule_faculty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='inside_room',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/room_picture/'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.CharField(choices=[('Computer Studies Department', 'Computer Studies Department')], default=None, max_length=50),
        ),
    ]
