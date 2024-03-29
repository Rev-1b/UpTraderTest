# Generated by Django 5.0.1 on 2024-02-01 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw_menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menumodel',
            options={'ordering': ['id'], 'verbose_name': 'Меню', 'verbose_name_plural': 'Меню'},
        ),
        migrations.RemoveField(
            model_name='menumodel',
            name='is_leaf',
        ),
        migrations.AlterField(
            model_name='menumodel',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название меню'),
        ),
        migrations.AlterField(
            model_name='menumodel',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Слаг'),
        ),
    ]
