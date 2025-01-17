# Generated by Django 5.0.1 on 2024-02-11 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_answer_stat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='code',
            field=models.TextField(default='# write your code here', max_length=3000, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='stat',
            field=models.CharField(choices=[('Все верно', 'Все верно'), ('Неверное решение', 'Неверное решение'), ('На проверке', 'На проверке')], default='Нет статуса', max_length=60, verbose_name='Статус кода'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='День рождение'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='groups',
            field=models.CharField(choices=[('Python 1', 'Python 1'), ('Python 2', 'Python 2'), ('Python 3', 'Python 3'), ('Python 4', 'Python 4')], max_length=20, verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pfp',
            field=models.ImageField(default='/profile_pics/default.png', upload_to='profile_pics', verbose_name='Аватарка'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='schedule_day',
            field=models.CharField(max_length=100, verbose_name='Расписание(дни)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='schedule_time',
            field=models.CharField(max_length=100, verbose_name='Расписание(часы)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='solved_problems',
            field=models.CharField(max_length=100, verbose_name='Решенные задачи'),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(auto_created=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(default='This is Default Description. Lorem ipsum dolor', max_length=8000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='difficulty',
            field=models.CharField(choices=[('1st Dan', '1st Dan'), ('2nd Dan', '2nd Dan'), ('3rd Dan', '3rd Dan'), ('4th Dan', '4th Dan'), ('5th Dan', '5th Dan')], default='1st Dan', max_length=10, verbose_name='Сложность'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(default='This is tasks title', max_length=80, verbose_name='Название'),
        ),
    ]
