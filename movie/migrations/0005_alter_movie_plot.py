# Generated by Django 4.0.5 on 2022-06-26 23:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_movie_cover_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='plot',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Trama'),
        ),
    ]
