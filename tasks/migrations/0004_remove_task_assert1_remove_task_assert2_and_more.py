# Generated by Django 4.2.5 on 2023-10-27 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_assert1_task_assert2_task_assert3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assert1',
        ),
        migrations.RemoveField(
            model_name='task',
            name='assert2',
        ),
        migrations.RemoveField(
            model_name='task',
            name='assert3',
        ),
        migrations.AddField(
            model_name='task',
            name='test',
            field=models.TextField(default='Введите тесты', max_length=10000),
        ),
    ]