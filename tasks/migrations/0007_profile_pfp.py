# Generated by Django 4.2.5 on 2023-12-04 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pfp',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]