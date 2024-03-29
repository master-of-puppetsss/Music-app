# Generated by Django 4.1.7 on 2023-02-23 14:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=120, verbose_name='Album name')),
                ('year', models.PositiveIntegerField(default=2023, validators=[django.core.validators.MinValueValidator(1951), django.core.validators.MaxValueValidator(2023)], verbose_name='Year of publication')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Singer')),
            ],
            options={
                'verbose_name': 'Singer',
                'verbose_name_plural': 'Singers',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=120, verbose_name='Song name')),
                ('singer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='songs.singer', verbose_name='Singer')),
            ],
            options={
                'verbose_name': 'Song',
                'verbose_name_plural': 'Songs',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='AlbumMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Ordinal number')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='songs.album', verbose_name='Album')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.song', verbose_name='Song')),
            ],
            options={
                'verbose_name': 'Song in albums',
                'verbose_name_plural': 'Songs in albums',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='songs.singer', verbose_name='Singer'),
        ),
        migrations.AddConstraint(
            model_name='albummembership',
            constraint=models.UniqueConstraint(fields=('song', 'album'), name='unique_song_number'),
        ),
        migrations.AddConstraint(
            model_name='albummembership',
            constraint=models.UniqueConstraint(fields=('album', 'number'), name='unique_album_number'),
        ),
        migrations.AddConstraint(
            model_name='album',
            constraint=models.UniqueConstraint(fields=('title', 'singer'), name='unique_title_singer'),
        ),
    ]
