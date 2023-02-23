from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from datetime import date


def get_current_year():
    return date.today().year


class Singer(models.Model):
    """Singer"""

    name = models.CharField(
        verbose_name='Singer',
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = 'Singer'
        verbose_name_plural = 'Singers'
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.name}'


class Album(models.Model):
    """Musical album"""

    title = models.CharField(
        verbose_name='Album name',
        max_length=120,
        db_index=True,
    )
    singer = models.ForeignKey(
        Singer,
        verbose_name='Singer',
        on_delete=models.CASCADE,
        related_name='albums',
    )
    year = models.PositiveIntegerField(
        verbose_name='Year of publication',
        default=get_current_year(),
        validators=[MinValueValidator(1951), MaxValueValidator(get_current_year())]
    )

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
        ordering = ['title']
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'singer'],
                name='unique_title_singer',
            )
        ]

    def __str__(self) -> str:
        return f'{self.title}'

    def clean(self):
        if not 1951 <= self.year <= get_current_year():
            raise ValidationError({
                'message': "year incorrect"
            })




class Song(models.Model):
    """Song"""

    title = models.CharField(
        verbose_name='Song name',
        max_length=120,
        db_index=True,
    )
    singer = models.ForeignKey(
        Singer,
        verbose_name='Singer',
        on_delete=models.CASCADE,
        related_name='songs',
        null=True
    )

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'
        ordering = ['title']

    def __str__(self) -> str:
        return f'{self.title}'


class AlbumMembership(models.Model):
    """Songs in album."""

    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        verbose_name='Song'
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        verbose_name='Album',
        related_name='songs',
    )

    number = models.PositiveSmallIntegerField(
        verbose_name='Ordinal number'
    )

    class Meta:
        verbose_name = 'Song in albums'
        verbose_name_plural = 'Songs in albums'
        constraints = [
            models.UniqueConstraint(
                fields=['song', 'album'],
                name='unique_song_number',
            ),
            models.UniqueConstraint(
                fields=['album', 'number'],
                name='unique_album_number',
            ),
        ]

    def __str__(self) -> str:
        return f'{self.number} - {self.song}'
