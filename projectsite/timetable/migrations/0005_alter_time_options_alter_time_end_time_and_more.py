# Generated by Django 4.2 on 2023-04-12 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0004_alter_time_end_time_alter_time_start_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='time',
            options={'verbose_name_plural': 'Time'},
        ),
        migrations.AlterField(
            model_name='time',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='time',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
