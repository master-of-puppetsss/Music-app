from django.core.exceptions import ValidationError
from django.db import DataError, IntegrityError
from django.test import TestCase

from songs.models import Singer, Album, Song, get_current_year


class SingerModelTest(TestCase):
    def test_name_max_length(self):
        with self.assertRaises(DataError):
            singer = Singer.objects.create(name='testname' * 7)

    def test_name_is_unique(self):
        with self.assertRaises(IntegrityError):
            singer_1 = Singer.objects.create(name='testname')
            singer_2 = Singer.objects.create(name='testname')


class AlbumModelTest(TestCase):
    def setUp(self):
        self.singer = Singer.objects.create(name='testname')

    def test_title_max_length(self):
        with self.assertRaises(DataError):
            Album.objects.create(title='testname' * 16, singer=self.singer, year=1955)

    def test_year_min_validator(self):
        album = Album.objects.create(title='testname', singer=self.singer, year=1950)
        with self.assertRaises(ValidationError):
            album.full_clean()

    def test_year_max_validator(self):
        next_year = get_current_year() + 1
        album = Album.objects.create(title='testname', singer=self.singer, year=next_year)
        with self.assertRaises(ValidationError):
            album.full_clean()


class SongModelTest(TestCase):
    def setUp(self):
        self.singer = Singer.objects.create(name='testname')
        self.album = Album.objects.create(title='testname', singer=self.singer, year=1955)

    def test_title_max_length(self):
        with self.assertRaises(DataError):
            song = Song.objects.create(title='testname' * 16, singer=self.singer)
            song.albums.set(self.album)

