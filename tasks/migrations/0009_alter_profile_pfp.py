# Generated by Django 4.2.5 on 2023-12-04 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_alter_profile_pfp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pfp',
            field=models.ImageField(default='/profile_pics/default.png', upload_to='profile_pics'),
        ),
    ]
