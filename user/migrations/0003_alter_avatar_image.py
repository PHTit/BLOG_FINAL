# Generated by Django 4.0.5 on 2022-06-27 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_avatar_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='staticfiles/avatars'),
        ),
    ]