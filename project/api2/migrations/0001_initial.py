# Generated by Django 5.0.1 on 2024-01-15 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО')),
                ('year', models.IntegerField(verbose_name='Возраст')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('year_release', models.IntegerField(verbose_name='Год выпуска')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api2.director', verbose_name='Режиссер')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api2.genre', verbose_name='Жанр')),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api2.film', verbose_name='Фильм')),
            ],
        ),
    ]
