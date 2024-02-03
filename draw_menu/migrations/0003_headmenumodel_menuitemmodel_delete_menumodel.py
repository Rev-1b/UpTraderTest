# Generated by Django 5.0.1 on 2024-02-01 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw_menu', '0002_alter_menumodel_options_remove_menumodel_is_leaf_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeadMenuModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название меню')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MenuItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название меню')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Слаг')),
                ('head_menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='draw_menu.headmenumodel', verbose_name='Ссылка на объект меню-хозяина')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='draw_menu.menuitemmodel', verbose_name='Элемент меню на уровень выше')),
            ],
            options={
                'verbose_name': 'Элемент меню',
                'verbose_name_plural': 'Элементы меню',
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='MenuModel',
        ),
    ]
