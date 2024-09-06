# Generated by Django 5.0.1 on 2024-02-11 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_alter_profile_solved_problems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='schedule_day',
            field=models.CharField(default='ПН-СР-ПТ', max_length=100, verbose_name='Расписание(дни)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='schedule_time',
            field=models.CharField(default='13:00-18:00', max_length=100, verbose_name='Расписание(часы)'),
        ),
    ]