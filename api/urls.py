from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'singers', views.SingerViewSet, basename="singers")
router.register(r'albums', views.AlbumViewSet, basename="albums")
router.register(r'songs', views.SongViewSet,basename="songs")
router.register(r'songs_in_albums', views.AlbumMembershipViewSet, basename='songs_in_albums')

urlpatterns = router.urls
