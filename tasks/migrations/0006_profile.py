# Generated by Django 4.2.5 on 2023-12-04 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0005_remove_task_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solved_problems', models.CharField(max_length=100)),
                ('groups', models.CharField(choices=[('Python 1', 'Python 1'), ('Python 2', 'Python 2'), ('Python 3', 'Python 3'), ('Python 4', 'Python 4')], max_length=20)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('schedule_day', models.CharField(max_length=100)),
                ('schedule_time', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
