# Generated by Django 4.2.5 on 2023-09-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_table',
            name='image',
            field=models.ImageField(default='sdsdsd', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
