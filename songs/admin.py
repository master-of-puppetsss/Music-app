from django.contrib import admin
from songs.models import Singer, Album, Song, AlbumMembership


@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'singer',
        'year',
    ]

    search_fields = ['title']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'singer',
    ]
    search_fields = ['title']

@admin.register(AlbumMembership)
class AlbumMembershipAdmin(admin.ModelAdmin):
    list_display = [
        'song',
        'album',
        'number',
    ]
    search_fields = ['song', 'album',]

