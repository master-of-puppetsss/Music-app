from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import SingerSerializer, ThinSingerSerializer, SongSerializer, AlbumSerializer, \
    AlbumMembershipSerializer
from songs.models import Album, Singer, Song, AlbumMembership


class SingerViewSet(ModelViewSet):
    """View for singer"""

    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

    def list(self, request, *args, **kwargs):
        singers = Singer.objects.all()
        context = {'request', request}
        serializer = ThinSingerSerializer(singers, many=True, context=context)
        return Response(serializer.data)


class AlbumViewSet(ModelViewSet):
    """View for album"""

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongViewSet(ModelViewSet):
    """View for song"""

    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumMembershipViewSet(ModelViewSet):
    """View for song in album"""

    queryset = AlbumMembership.objects.all()
    serializer_class = AlbumMembershipSerializer
