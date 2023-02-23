from typing import List

from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from songs.models import Singer, Song, Album, AlbumMembership


class SingerSerializer(serializers.ModelSerializer):
    """Serializer for singer detail"""
    albums_id = serializers.SerializerMethodField()

    def get_albums_id(self, obj: Singer) -> List[str]:
        return [album.title for album in obj.albums.all()]

    class Meta:
        model = Singer
        fields = ('id', 'name', 'albums_id')


class ThinSingerSerializer(serializers.ModelSerializer):
    """Serializer for singer list"""
    class Meta:
        model = Singer
        fields = ('id', 'name',)


class AlbumSerializer(serializers.ModelSerializer):
    """Serializer for list albums"""
    singer = serializers.CharField(max_length=50)

    def get_singer(self, obj: Album) -> str:
        return f'{obj.singer}'

    def create(self, validated_data: dict):
        """Methods for create album"""
        singer_name = validated_data.pop('singer')
        singer_instance, _ = Singer.objects.get_or_create(name=singer_name)
        obj = Album.objects.create(**validated_data, singer=singer_instance)
        return obj

    class Meta:
        model = Album
        fields = (
            'id',
            'title',
            'singer',
            'year',
        )


class SongSerializer(serializers.ModelSerializer):
    """Serializer for Song"""

    singer = serializers.CharField(max_length=50)

    def get_singer(self, obj):
        return str(obj.singer)

    def create(self, validated_data: dict):
        """Methods for create song"""
        singer_name = validated_data.pop('singer')
        sing_instance, _ = Singer.objects.get_or_create(name=singer_name)
        obj = Song.objects.create(**validated_data, singer=sing_instance)
        return obj

    class Meta:
        model = Song
        fields = (
            'id',
            'title',
            'singer',
        )


class AlbumMembershipSerializer(serializers.ModelSerializer):
    """Serializer for AlbumMembership"""

    album = serializers.CharField(max_length=120)
    song = serializers.CharField(max_length=120)

    def get_album(self, obj):
        return f'{obj.album}'

    def get_song(self, obj):
        return f'{obj.song}'

    @transaction.atomic
    def create(self, validated_data: dict):
        """Methods for create song in album"""
        album_title = validated_data.pop('album')
        song_title = validated_data.pop('song')
        album_instance = Album.objects.filter(title=album_title).first()
        if not album_instance:
            raise serializers.ValidationError('Such an album does not exist')
        song_instance, _ = Song.objects.get_or_create(title=song_title)
        obj = AlbumMembership.objects.create(
            **validated_data, album=album_instance, song=song_instance
        )
        return obj

    class Meta:
        model = AlbumMembership
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=AlbumMembership.objects.all(),
                fields=['song', 'album'],
                message='This song is already on the album',
            ),
            UniqueTogetherValidator(
                queryset=AlbumMembership.objects.all(),
                fields=['album', 'number'],
                message='The serial number of the song on the album already exists',
            )]
