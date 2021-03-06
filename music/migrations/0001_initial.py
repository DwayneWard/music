# Generated by Django 4.0.3 on 2022-07-12 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Подборка',
                'verbose_name_plural': 'Подборки',
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('author', models.CharField(max_length=50, verbose_name='Исполнитель')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Дата выхода')),
                ('genre', models.CharField(max_length=50, verbose_name='Жанр')),
                ('duration_in_seconds', models.IntegerField(verbose_name='Длительность в секундах')),
                ('album', models.CharField(max_length=50, verbose_name='Альбом')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Обложка')),
                ('track_file', models.FileField(upload_to='music_files', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Трек',
                'verbose_name_plural': 'Треки',
            },
        ),
    ]
