# Generated by Django 5.0.1 on 2024-02-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_task_input_data_task_output_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='input_data',
            field=models.TextField(default='Введите входные данные', max_length=100, verbose_name='Входные данные'),
        ),
        migrations.AlterField(
            model_name='task',
            name='output_data',
            field=models.TextField(default='Введите выходные данные', max_length=100, verbose_name='Выходные данные'),
        ),
    ]
