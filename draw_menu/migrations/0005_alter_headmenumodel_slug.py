# Generated by Django 5.0.1 on 2024-02-02 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw_menu', '0004_headmenumodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headmenumodel',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Слаг'),
        ),
    ]
