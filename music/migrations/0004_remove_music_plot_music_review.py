# Generated by Django 4.0.5 on 2022-06-27 17:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_music_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='plot',
        ),
        migrations.AddField(
            model_name='music',
            name='review',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Reseña'),
        ),
    ]