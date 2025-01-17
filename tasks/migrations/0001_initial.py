# Generated by Django 4.2.5 on 2023-09-25 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_created=True)),
                ('title', models.CharField(default='This is tasks title', max_length=80)),
                ('description', models.TextField(default='This is Default Description. Lorem ipsum dolor', max_length=800)),
                ('difficulty', models.CharField(choices=[('1st Dan', '1st Dan'), ('2nd Dan', '2nd Dan'), ('3rd Dan', '3rd Dan'), ('4th Dan', '4th Dan'), ('5th Dan', '5th Dan')], default='1st Dan', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(default='# write your code here', max_length=3000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]
