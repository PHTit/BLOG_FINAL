# Generated by Django 4.0.5 on 2022-06-26 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_alter_movie_plot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles/covers/', verbose_name='Poster'),
        ),
    ]