# Generated by Django 4.0.5 on 2022-06-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_remove_game_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles/covers/', verbose_name='Poster'),
        ),
    ]
